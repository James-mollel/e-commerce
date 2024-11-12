document.addEventListener("DOMContentLoaded",function(){
  displayCartItems();
});


function addToCart(id, name, price, image,button){

  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  const existingProduct = cart.find(item => item.id === id);
  if (existingProduct){
    existingProduct.quantity +=1;
  }else{
    cart.push({id, name, price, image,quantity: 1});
  }
  localStorage.setItem("cart",JSON.stringify(cart));
  button.textContent = 'Added'
  button.style.background = 'green'
}

// function display cart items 

function displayCartItems(){
  const cartItemsContainer = document.getElementById('cart-items-container');
  const cart = JSON.parse(localStorage.getItem('cart')) || [];
  cartItemsContainer.innerHTML = '';
  

  if(cart.length === 0){
    cartItemsContainer.innerHTML = "<p> Your Cart is empty. </p>";
    document.getElementById('total-price').textContent = "0.0";
  }else{
    let totalPrice = 0;
    cart.forEach(item => {
      const itemElement = document.createElement('div');
      itemElement.classList.add("cart-item");

      itemElement.innerHTML =` <img src="${item.image}" alt="${item.name}">
       <div class="item-details">
  <p class="item-name">${item.name}</p>
  <p class="item-price">Tsh: ${item.price} x ${item.quantity}</p>
  <div class="quantity-controls">
    <button onclick="decreaseQuantity(${item.id})">-</button>
    <span>${item.quantity}</span>
    <button onclick="increaseQuantity(${item.id})">+</button>
  </div>
 </div>
      `;
      cartItemsContainer.appendChild(itemElement);
      totalPrice += item.price * item.quantity;
      
    });
    document.getElementById('total-price').textContent = totalPrice.toFixed(2)
  }
}


// increase quantity of product 

function increaseQuantity(id){
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  const product  = cart.find(item => item.id === id);

  if (product){
    product.quantity += 1;
    localStorage.setItem("cart", JSON.stringify(cart));
    displayCartItems();
  }
}

function decreaseQuantity(id){
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  const product  = cart.find(item => item.id === id);

  if (product){
    product.quantity -= 1;
    if (product.quantity <=0 ){
      cart = cart.filter(item => item.id !== id);
    }
    localStorage.setItem("cart", JSON.stringify(cart));
    displayCartItems();
  }
}

function sendOrder(){
  const cart = JSON.parse(localStorage.getItem("cart")) || [];
  if (cart.length === 0){
    alert("Your cart is empty ");
    return;
  }
  let orderMessage = "Order Details: \n";
  total = 0;
  url_image = 'https://e-commerce-10sy.onrender.com'
  cart.forEach(item =>{
    orderMessage += `\n Product: '${item.name}' \n Quantity: ${item.quantity}\n `
    orderMessage += `Price: ${item.price}\n`
    orderMessage += `Image:${url_image+item.image}\n`
    total += item.price * item.quantity;
  });
  orderMessage += `\n Total: Tsh:${total}`;
  
  const order_number=  phone_Numbers[0]
  const whatsuppMessage = encodeURIComponent(orderMessage)
  const whatsupp_url = `https://wa.me/${order_number}?text=${whatsuppMessage}`;
  window.open(whatsupp_url,"_blank");
  localStorage.removeItem("cart");
}


if(document.getElementById("cart-items-container")){
  displayCartItems();
}