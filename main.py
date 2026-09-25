from pyscript import document, display



def place_order(e):       #put e for the event handler   
    document.getElementById("output1").innerHTML = "" #clears result

    name = document.getElementById("cn").value #gets user's inputted name



    coffee = document.getElementById("cofs")  #gets or calls the value of the coffee selected
    coffee_price = float(coffee.value)  

    size = document.querySelector("input[name='size']:checked") #checked is to see if a size is selected
    price = float(size.value) 
 
    subtotal = coffee_price + price #adds the coffee price and price we called to get subtotal

    tax = 0.12

    vat = tax * subtotal #multiplies tax rate to subtotal to get VAT

    total = vat + subtotal #adds VAT and subtotal to get overall total


#displays subtotal, VAT, total, and customer's name
    display(f'Your subtotal is: ₱{subtotal}', target="output1")
    display(f'VAT: ₱{vat}', target="output1", append=True)   
    display(f'Total Amount: ₱{total}', target="output1", append=True)
    display(f'Enjoy your drink, {name}! :)', target="output1", append=True)

