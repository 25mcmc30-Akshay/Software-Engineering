from flask import Flask, render_template, request, make_response
from database import get_connection
from datetime import datetime, timedelta
import pdfkit

app = Flask(__name__)

config = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
)


def calculate_bill(units):

    if units <= 50:
        amount = units * 1.75

    elif units <= 100:
        amount = (50 * 1.75) + ((units - 50) * 3)

    elif units <= 150:
        amount = (
            (50 * 1.75)
            + (50 * 3)
            + ((units - 100) * 4.25)
        )

    elif units <= 200:
        amount = (
            (50 * 1.75)
            + (50 * 3)
            + (50 * 4.25)
            + ((units - 150) * 5.5)
        )

    else:
        amount = (
            (50 * 1.75)
            + (50 * 3)
            + (50 * 4.25)
            + (50 * 5.5)
            + ((units - 200) * 7.5)
        )

    return amount


@app.route('/')
def home():
    return render_template("index.html")


# ================= SEARCH CONSUMER =================

@app.route('/search', methods=['POST'])
def search():

    consumer_no = request.form['consumer_no']

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM consumers
        WHERE consumer_no = %s
        """,
        (consumer_no,)
    )

    consumer = cursor.fetchone()

    cursor.close()
    conn.close()

    if not consumer:
        return "<h2>Consumer Not Found</h2>"

    return render_template(
        'consumer.html',
        consumer=consumer
    )


# ================= GENERATE BILL =================

@app.route('/generate_bill', methods=['POST'])
def generate_bill():

    consumer_no = request.form['consumer_no']
    units = int(request.form['units'])

    amount = calculate_bill(units)

    bill_no = (
        f"BILL{consumer_no}"
        f"{datetime.now().strftime('%Y%m%d%H%M%S')}"
    )

    bill_date = datetime.today().date()
    due_date = bill_date + timedelta(days=15)

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Previous Due

    cursor.execute(
        """
        SELECT payable_amount
        FROM bills
        WHERE consumer_no=%s
        ORDER BY bill_date DESC
        LIMIT 1
        """,
        (consumer_no,)
    )

    last_bill = cursor.fetchone()

    if last_bill:
        previous_due = float(last_bill['payable_amount'])
    else:
        previous_due = 0.0

    current_bill = float(amount)

    payable_amount = previous_due + current_bill

    bill_month = datetime.today().strftime("%B")

    # Save Bill

    cursor.execute(
        """
        INSERT INTO bills
        (
            bill_no,
            consumer_no,
            bill_month,
            bill_date,
            due_date,
            units,
            previous_due,
            current_bill,
            payable_amount
        )
        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            bill_no,
            consumer_no,
            bill_month,
            bill_date,
            due_date,
            units,
            previous_due,
            current_bill,
            payable_amount
        )
    )

    conn.commit()

    # Consumer Details

    cursor.execute(
        """
        SELECT *
        FROM consumers
        WHERE consumer_no=%s
        """,
        (consumer_no,)
    )

    consumer = cursor.fetchone()

    bill = {
        "bill_no": bill_no,
        "bill_date": bill_date,
        "due_date": due_date,
        "consumer_no": consumer["consumer_no"],
        "consumer_name": consumer["consumer_name"],
        "address": consumer["address"],
        "mobile": consumer["mobile"],
        "email": consumer["email"],
        "division": consumer["division"],
        "sanctioned_load": consumer["sanctioned_load"],
        "meter_no": consumer["meter_no"],
        "connection_date": consumer["connection_date"],
        "units": units,
        "current_bill": current_bill,
        "previous_due": previous_due,
        "payable_amount": payable_amount
    }

    cursor.close()
    conn.close()

    return render_template(
        "bill.html",
        bill=bill,
        pdf_mode=False
    )


# ================= DOWNLOAD PDF =================

@app.route('/download_pdf/<bill_no>')
def download_pdf(bill_no):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT
            b.*,
            c.consumer_name,
            c.address,
            c.mobile,
            c.email,
            c.division,
            c.sanctioned_load,
            c.meter_no,
            c.connection_date
        FROM bills b
        JOIN consumers c
        ON b.consumer_no = c.consumer_no
        WHERE b.bill_no = %s
        """,
        (bill_no,)
    )

    bill = cursor.fetchone()

    cursor.close()
    conn.close()

    if not bill:
        return "Bill Not Found"

    html = render_template(
        "bill.html",
        bill=bill,
        pdf_mode=True,
        logo_url="http://127.0.0.1:5000/static/images/logo.png"
    )

    options = {
        "enable-local-file-access": "",
        "load-error-handling": "ignore",
        "load-media-error-handling": "ignore",
        "page-size": "A4",
        "orientation": "Portrait",
        "encoding": "UTF-8",
        "margin-top": "3mm",
        "margin-bottom": "3mm",
        "margin-left": "3mm",
        "margin-right": "3mm",
        "print-media-type": ""
    }

    pdf = pdfkit.from_string(
        html,
        False,
        configuration=config,
        options=options
    )

    response = make_response(pdf)

    response.headers["Content-Type"] = "application/pdf"

    response.headers["Content-Disposition"] = (
        f"attachment; filename={bill_no}.pdf"
    )

    return response


if __name__ == "__main__":
    app.run(debug=True)
    
 
