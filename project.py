from pyscript import document, display

def place_order (e):
    document.getElementById("output1").innerHTML = ""
    prod1 = document.getElementById("prod1")
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
    size = document.querySelector("input[name='size']:checked")
    price = float(size.value)
    subtotal = price + prod1 + prod2 + prod3 + prod4 + prod5 + prod6 + prod7 + prod8
    tax = subtotal * 0.12
    total = subtotal + tax
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
    category = document.getElementById("cat").value
    product = document.getElementById("prod").value
    quantity = document.getElementById("quan").value 
    sku = category[:3].upper() + "-" + product[:4].upper() + "-" + str(quantity)
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
    