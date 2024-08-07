import { getProductsData, getSizes } from "./api.js";

const url = window.location.href;
const productId = url.match(/\/detalle-producto\/(\d+)\//)[1];
let cartItem = {
    quantity: null,
    size: null,
    id: productId
};

if (productId) {
    console.log(`ID del producto: ${productId}`);

    function mapProducts(products, brands, categories) {
        const brandMap = {};
        const categoryMap = {};
        brands.forEach(brand => {
            brandMap[brand.id] = brand.name;
        });
        categories.forEach(category => {
            categoryMap[category.id] = category.name;
        });
        const mappedProducts = products.map(product => ({
            ...product,
            brand_name: brandMap[product.brand_id],
            category_name: categoryMap[product.category_id]
        }));
        return mappedProducts;
    }

    const locationInfoProduct = document.getElementById("infoProduct");

    const loadInformation = (results = {}) => {
        const name = results.name;
        const price = results.price;
        const brand = results.brand_name;
        const stock = results.quantity;
        const url = results.image_url;
        console.log(url);
        const row = document.createElement("div");
        row.classList.add("row");

        const col = document.createElement("div");
        col.classList.add("col");

        const image = document.createElement("img");
        image.src = url;
        image.classList.add("w-100");
        image.classList.add("h-100");

        col.appendChild(image);

        const colBody = document.createElement("div");
        colBody.classList.add("col");
        colBody.id = "productDetail";

        const title = document.createElement("h1");
        title.textContent = name;

        const pa = document.createElement("p");
        pa.textContent = brand;

        const titlePrice = document.createElement("h3");
        titlePrice.textContent = `$${price}`;

        const productInfo = document.createElement("div");
        productInfo.id = "productInfo";
        productInfo.appendChild(pa);
        productInfo.appendChild(titlePrice);

        const selecterInfo = document.createElement("div");
        selecterInfo.id = "selecterInfo";

        const dropdownDiv = document.createElement("div");
        dropdownDiv.classList.add("dropdown");

        const dropdownButton = document.createElement("button");
        dropdownButton.classList.add("btn", "btn-secondary", "dropdown-toggle");
        dropdownButton.type = "button";
        dropdownButton.id = "sizeDropdownButton"; // Asignar ID
        dropdownButton.setAttribute("data-bs-toggle", "dropdown");
        dropdownButton.setAttribute("aria-expanded", "false");
        dropdownButton.textContent = "Tallas";

        const dropdownMenu = document.createElement("ul");
        dropdownMenu.classList.add("dropdown-menu");
        dropdownMenu.id = "sizeDropdownMenu";

        dropdownDiv.appendChild(dropdownButton);
        dropdownDiv.appendChild(dropdownMenu);

        const quantityDropdownDiv = document.createElement("div");
        quantityDropdownDiv.classList.add("dropdown");

        const quantityDropdownButton = document.createElement("button");
        quantityDropdownButton.classList.add("btn", "btn-secondary", "dropdown-toggle");
        quantityDropdownButton.type = "button";
        quantityDropdownButton.id = "quantityDropdownButton"; // Asignar ID
        quantityDropdownButton.setAttribute("data-bs-toggle", "dropdown");
        quantityDropdownButton.setAttribute("aria-expanded", "false");
        quantityDropdownButton.textContent = "Cantidad";

        const quantityDropdownMenu = document.createElement("ul");
        quantityDropdownMenu.classList.add("dropdown-menu");
        quantityDropdownMenu.id = "quantityDropdownMenu";
        quantityDropdownDiv.appendChild(quantityDropdownButton);
        quantityDropdownDiv.appendChild(quantityDropdownMenu);

        selecterInfo.appendChild(quantityDropdownDiv);

        for (let i = 1; i <= stock; i++) {
            const option = document.createElement("li");
            const link = document.createElement("a");
            link.classList.add("dropdown-item");
            link.href = "#";
            link.textContent = i;
            link.dataset.quantity = i;

            link.addEventListener('click', function(event) {
                event.preventDefault();
                const selectedQuantity = parseInt(event.target.dataset.quantity);
                cartItem.quantity = selectedQuantity;
                console.log(`Seleccionada cantidad: ${selectedQuantity}`);
                quantityDropdownButton.textContent = `Cantidad: ${selectedQuantity}`;
            });

            option.appendChild(link);
            quantityDropdownMenu.appendChild(option);
        }

        const addToCartButton = document.createElement("button");
        addToCartButton.id = "ShoppingCartButton";
        addToCartButton.classList.add("btn", "btn-dark", "mt-3");
        addToCartButton.textContent = "Agregar al Carrito";
        addToCartButton.addEventListener('click', function() {
            if (cartItem.quantity !== null && cartItem.size !== null) {
                const data = {
                    quantity: cartItem.quantity,
                    size: cartItem.size,
                    productId: cartItem.id
                };
        
                const url = `/web/api/agregar-al-carrito/${cartItem.id}/${cartItem.quantity}/${cartItem.size}/`; // Ajusta la URL según tu endpoint de API
                const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content'); // Obtener el token CSRF
        
                fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken
                    },
                    body: JSON.stringify(data)
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Error al agregar al carrito');
                    }
                    return response.json();
                })
                .then(data => {
                    alert('Producto agregado exitosamente');
                    location.reload();
                })
                .catch(error => {
                    console.error('Error al agregar al carrito:', error);
                });
            } else {
                console.error('Debe seleccionar cantidad y talla antes de agregar al carrito');
            }
        });

        colBody.appendChild(title);
        colBody.appendChild(productInfo);
        colBody.appendChild(selecterInfo);
        selecterInfo.appendChild(dropdownDiv);
        colBody.appendChild(addToCartButton);

        locationInfoProduct.appendChild(col);
        locationInfoProduct.appendChild(colBody);
    };

    getProductsData()
        .then((data) => {
            const results = mapProducts(data.products, data.brands, data.categories);
            const product = results.find(product => product.id === parseInt(productId));

            loadInformation(product);
            getSizes()
                .then((sizes) => {
                    const dropdownMenu = document.querySelector('#sizeDropdownMenu');
                    const dropdownButton = document.querySelector('#sizeDropdownButton'); // Definir dropdownButton por ID

                    sizes.forEach(size => {
                        const option = document.createElement('li');
                        const link = document.createElement('a');
                        link.classList.add('dropdown-item');
                        link.href = '#';
                        link.textContent = size.size_name;
                        link.dataset.sizeId = size.id;

                        link.addEventListener('click', function(event) {
                            event.preventDefault();
                            const selectedSize = event.target.textContent;
                            cartItem.size = selectedSize;
                            console.log(`Seleccionada talla: ${selectedSize}`);
                            dropdownButton.textContent = `Talla: ${selectedSize}`;  // Actualizar el texto del botón
                        });

                        option.appendChild(link);
                        dropdownMenu.appendChild(option);
                    });
                    const dropdownToggleButtons = document.querySelectorAll('.dropdown-toggle');
                    dropdownToggleButtons.forEach(button => new bootstrap.Dropdown(button));

                })
                .catch((error) => {
                    console.error('Error al obtener los tamaños:', error);
                });
        })
        .catch((error) => {
            console.error(`Error al obtener los datos del producto: ${error}`);
        });

} else {
    console.error('No se pudo obtener el ID del producto desde la URL');
}
