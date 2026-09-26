from pyscript import document, display

def place_order (e):
    document.getElementById("output1").innerHTML = ""
    prod1 = document.getElementById("prod1") #gets the value of the checkbox and verifies if checked by the user
    prod1 = float(prod1.value) * prod1.checked
    prod2 = document.getElementById("prod2")
    prod2 = float(prod2.value) * prod2.checked
    prod3 = document.getElementById("prod3")
    prod3 = float(prod3.value) * prod3.checked
    prod4 = document.getElementById("prod4")
    prod4 = float(prod4.value) * prod4.checked
    prod5 = document.getElementById("prod5")
    prod5 = float(prod5.value) * prod5.checked
    prod6 = document.getElementById("prod6")
    prod6 = float(prod6.value) * prod6.checked
    prod7 = document.getElementById("prod7")
    prod7 = float(prod7.value) * prod7.checked
    prod8 = document.getElementById("prod8")
    prod8 = float(prod8.value) * prod8.checked
    size = document.querySelector("input[name='size']:checked") #selects input values with the name 'size' and checks if they were clicked by the user
    price = float(size.value)
    subtotal = price + prod1 + prod2 + prod3 + prod4 + prod5 + prod6 + prod7 + prod8 #sums all the values of the user's CHECKED input fields
    tax = subtotal * 0.12 #derives the tax gained by how many products were checked
    total = subtotal + tax #adds tax to subtotal to get the final price
    #receipt processing through the f string for more clarity and authentic look; displays prices rounded down so that there are no repeating decimal prices
    document.getElementById("output1").innerHTML = f''' 
    ----------------------------------------------------
    <br>
    <h2><b>***RECEIPT***</b></h2>
    ----------------------------------------------------
    <div class="container" style="text-align: left;">
    <br>
    SUBTOTAL: P{subtotal//1} 
    <br>
    TAX: P{tax//1} 
    <br>
    TOTAL: P{total//1} 
    <br><br>
    </div>
    -----------------------------------------------------
    <br>
    Thank you for your order, User141!
    <br>
    Please come again.
    '''


def show_sku (e):
    document.getElementById("output2").innerHTML = ""
    category = document.getElementById("cat").value #gets the string value of the dropdown select field
    product = document.getElementById("prod").value #gets the string value from the user's own input
    quantity = document.getElementById("quan").value #gets integer value from the number input field
    sku = category[:3].upper() + "-" + product[:4].upper() + "-" + str(quantity) #targets specific letters from each input and combines it to form the SKEW
    #SKU shown in tabular format to organize the inputs of the user
    document.getElementById("output2").innerHTML = f'''
    
    <table class="table" style="font-family: 'Courier New', Courier, monospace;">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Category</th>
      <th scope="col">Product</th>
      <th scope="col">Quantity</th>
      <th scope="col">SKU</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃</th>
      <td>{category}</td>
      <td>{product}</td>
      <td>{quantity}</td>
      <td><b>{sku}</b></td>
    </tr>
    </tbody>
    </table>'''
