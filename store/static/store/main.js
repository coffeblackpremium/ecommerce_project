let carts = document.querySelectorAll("[id^='add-cart']")

let products = [
    {
        name: 'Produto 1',
        tag: 'produto1',
        price: 15,
        inCart: 0
    },
    {
        name: 'Produto 2',
        tag: 'produto2',
        price: 20,
        inCart: 0
    },
    {
        name: 'Produto 3',
        tag: 'produto3',
        price: 30,
        inCart: 0
    },
]

for(let i=0; i < carts.length; i++){
    carts[i].addEventListener('click', () => {
        cartNumbers(products[i])
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
    
    
    if(cartItems != null){
        cartItems[product.tag].inCart += 1
    } else {
        product.inCart = 1
        cartItems = {
            [product.tag]: product
        }
    }

    product.inCart = 1

    cartItems = {
        [product.tag]: product
    }

    localStorage.setItem('productsInCart', JSON.stringify(cartItems))
}

onLoadCartNumbers()