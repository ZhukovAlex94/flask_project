from faker import Faker

f = Faker()


@app.route('/get_name')
def get_name():
    first_name = f.first_name()
    last_name = f.last_name()
    return f"Person: {first_name} {last_name}"
