from datetime import datetime
from flask import make_response, abort

#timestamp creates in-memory structure
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

#Data to serve via API

customers = {
    "Smith": {'id': 1,
     'name': 'Jon Smith',
     'phone_number': '07717751950',
     'timestamp': get_timestamp()},
    "George": {'id': 2,
     'name': 'Lord George',
     'phone_number': '123456789',
     'timestamp': get_timestamp()},
    "Api": {'id': 3,
     'name': 'Jason Appi',
     'phone_number': '02086668888',
     'timestamp': get_timestamp()},
    "Doe": {'id': 4,
     'name': 'John Doe',
     'phone_number': '55588880',
     'timestamp': get_timestamp()},
    "Showers": {'id': 5,
     'name': 'April Showers',
     'phone_number': '234578901',
     'timestamp': get_timestamp()}
}

def read():
    """
    Respond to the request for /api/customers
    with the complete list of customers.

    :return: list of customers
    """
    #create a full list of customers from Data
    return [customers[key] for key in sorted(customers.keys())]

def read_id(id):
    """
    This function responds to a request for /api/customers/{id}
    with one matching customer from Customers

    :param id: id of customer
    :return:   customer matching id
    """
    #does the id exist?
    if id in customers:
        customer = customers.get(id)

    #not found
    else:
        abort(404, 'Customer with id {0} not found'.format(id))

    return customer

def read_name(name):
    """
    This function responds to a request for /api/customers/{name}
    with one matching customer from Customers

    :param name: name of customer
    :return:   customer matching name
    """
    #does the name exist?
    #e.g., [url]/api/customers/Smith
    if name in customers:
        customer = customers.get(name)

    #not found
    else:
        abort(404, 'Customer with name {0} not found'.format(name))

    return customer

  def addPhone(phone_number):
      """
      Activates a phone number in the customer data structure

      :param name:         name of customer to update
      :param phone_number: phone number to add
      :return:             updated structure
      """

      #does the customer exist?
      if name in customers:
          customers[name]['phone_number'] = customer.get('phone_number')
          customers[name] = get_timestamp()

         #otherwise an error
     else:
         abort(404, 'person with {0} not found'.format(name))
