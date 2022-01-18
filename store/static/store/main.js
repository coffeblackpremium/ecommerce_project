
let carts = document.querySelectorAll("[id^='add-cart']")

let products = [
    {
        name: 'Produto 1',
        tag: 'produto1',
        price: 15,
        inCart: 0,
    },
    {
        name: 'Produto 2',
        tag: 'produto2',
        price: 20,
        inCart: 0,
    },
    {
        name: 'Produto 3',
        tag: 'produto3',
        price: 30,
        inCart: 0,
    },
]

for(let i=0; i < carts.length; i++){
    carts[i].addEventListener('click', () => {
        cartNumbers(products[i])
        totalCost(products[i])
    })
}

function onLoadCartNumbers() {
    let productNumbers = localStorage.getItem('cartNumbers')

    if(productNumbers) {
        document.querySelector("[id^='cart-total']").textContent = productNumbers
    }
}

function cartNumbers(product) {
    
    let productNumbers = localStorage.getItem('cartNumbers')

    productNumbers = parseInt(productNumbers)
    if (productNumbers) {
        localStorage.setItem('cartNumbers', productNumbers + 1)
        document.querySelector("[id^='cart-total']").textContent = productNumbers + 1

    }else {
        localStorage.setItem('cartNumbers', 1)
        document.querySelector("[id^='cart-total']").textContent = 1
    }

    setItems(product)
}

function setItems(product) {
    let cartItems = localStorage.getItem('productsInCart')
    cartItems = JSON.parse(cartItems)
    if(cartItems != null ){
        if(cartItems[product.tag] == undefined){
            cartItems = {
                ...cartItems,
                [product.tag]: product
            }
        }
        cartItems[product.tag].inCart += 1
    } else {
        product.inCart = 1
        cartItems = {
            [product.tag]: product
        }
    }

    localStorage.setItem('productsInCart', JSON.stringify(cartItems))
}

function totalCost(product) {
    let cartCost = localStorage.getItem('totalCost')


    if(cartCost != null){
        cartCost = parseInt(cartCost)
        localStorage.setItem('totalCost', cartCost + product.price)
    } else {
        localStorage.setItem('totalCost', product.price)
    }
}

function displayCart() {
    let cartItems = localStorage.getItem('productsInCart')
    cartItems = JSON.parse(cartItems)
    let productContainer = document.querySelector(".products")
    let cartCost = localStorage.getItem('totalCost')

    console.log(cartItems)
    if(cartItems && productContainer){
        productContainer.innerHTML = ''
        Object.values(cartItems).map(item => {
            productContainer.innerHTML += `
            
            <div class="product>
                <i class="fas fa-times-circle"></i>
                <i class="fas fa-times-circle"></i>
                <img class="img-product-cart" src="../static/store/img/${item.tag}.jpg" />
                <span>${item.name}</span>
            </div>
            <div class="price">Preço: R$${item.price}</div>
            <div class="quantity">
                <i class="fas fa-angle-left"></i>
                <span>${item.inCart}</span>
                <i class="fas fa-angle-right"></i>
            </div>
            <div class="total">
               Preço Total: ${item.inCart * item.price}
            </div>
        
        `
        })
    }
}
onLoadCartNumbers()
displayCart()