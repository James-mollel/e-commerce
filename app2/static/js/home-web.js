








// // get the element 
// const BuynowBtn = document.querySelectorAll('.add-to-cart');
// const popup = document.getElementById('popup');
// // const productName = document.querySelectorAll('.names'); 
// const closeBtn = document.getElementById('close-popup');
// const productNameInput = document.getElementById('product-name');

const date_val = document.getElementById('copy')

const Year = new Date()
date_val.innerHTML = Year.getFullYear()

// slides here 
const slider = document.querySelector('.slider');
let currentIndex = 0;

function autoSlide(){
  const slides = document.querySelectorAll('.slide');
  currentIndex = (currentIndex + 1) % slides.length;
  slider.style.transform = `translateX(-${currentIndex * 100}%)`;
}

setInterval(autoSlide, 3000);
// slider here 

// // opne poup 
// BuynowBtn.forEach(button => {
// button.addEventListener('click',(event)=>{
//   const productName = event.target.closest('.product-card').querySelector('.names').textContent;
//   productNameInput.value = productName;
//   popup.style.display = 'block';
// });
// });

// // close popup
// closeBtn.addEventListener('click',()=>{
// popup.style.display = 'none';
// });

// // close poup when click othe side of window 
// window.addEventListener('click',(event)=>{
// if(event.target === popup){
//   popup.style.display = 'none';
// }
// });
