import { getProductsData } from "./api.js";

const locationProducts = document.getElementById("loadProducts");
const locationSale = document.getElementById("productsSection");
const loadMoreButton = document.getElementById("loadMoreBtn");

let loadedProducts = [];
let startIndex = 0;
let allProductsRendered = false;
const itemPage = 5;

// Función para mostrar la sección de ventas
const saleSection = (products) => {
    const stockProducts = products.length;
    const stockP = document.createElement("h3");
    stockP.textContent = `${stockProducts} ARTICULOS`;

    const saleText = document.createElement("h3");
    saleText.textContent = "SALE";

    locationSale.appendChild(stockP);
    locationSale.appendChild(saleText);

};

// Funcion para mostrar todos los productos en el DOM
const showAllProducts = (results = []) => {
    if (results.length > 0) {
        results.forEach(product => {
            const id = product.id;
            const name = product.name.toUpperCase();
            const stock = product.quantity;
            const price = product.price;

            const row = document.createElement("div");
            row.classList.add("row");
            row.addEventListener("click", () => {
                window.location.href = `/web/api/detalle-producto/${id}/`;  // Redirecciona al detalle del producto
            });
            const card = document.createElement("div");
            card.classList.add("card");

            const img = document.createElement("img");
            img.src = `../media/${product.image}`;
            img.classList.add("card-img-top");

            const cardBody = document.createElement("div");
            cardBody.classList.add("card-body");

            const cardTitle = document.createElement("h5");
            cardTitle.classList.add("card-title");
            cardTitle.textContent = name;

            const cardPrice = document.createElement("p");
            cardPrice.classList.add("card-text");
            cardPrice.textContent = `$ ${price}`;

            const cardCategory = document.createElement("p");
            cardCategory.classList.add("card-text");
            cardCategory.textContent = `Solo quedan ${stock} unidades disponibles!!`;

            cardBody.appendChild(cardTitle);
            cardBody.appendChild(cardPrice);
            cardBody.appendChild(cardCategory);

            card.appendChild(img);
            card.appendChild(cardBody);

            row.appendChild(card);
            locationProducts.appendChild(row);
        });
    } else {
        alert("No hay productos disponibles con los filtros seleccionados.");
        location.reload();
    }
};
// Función para mostrar productos por 5 en el DOM
const showProducts = (results = [], startIndex) => {
    const endIndex = startIndex + itemPage;
    if (results.length > 0) {
        for (let i = startIndex; i < endIndex && i < results.length; i++) {
            const product = results[i];
            const id = product.id;
            const name = product.name.toUpperCase();
            const stock = product.quantity;
            const price = product.price;

            const row = document.createElement("div");
            row.classList.add("row");
            row.addEventListener("click", () => {
                window.location.href = `/web/api/detalle-producto/${id}/`;  // Redirecciona al detalle del producto
            });
            const card = document.createElement("div");
            card.classList.add("card");

            const img = document.createElement("img");
            img.src = `../media/${product.image}`;
            img.classList.add("card-img-top");

            const cardBody = document.createElement("div");
            cardBody.classList.add("card-body");

            const cardTitle = document.createElement("h5");
            cardTitle.classList.add("card-title");
            cardTitle.textContent = name;

            const cardPrice = document.createElement("p");
            cardPrice.classList.add("card-text");
            cardPrice.textContent = `$ ${price}`;

            const cardCategory = document.createElement("p");
            cardCategory.classList.add("card-text");
            cardCategory.textContent = `Solo quedan ${stock} unidades disponibles!!`;

            cardBody.appendChild(cardTitle);
            cardBody.appendChild(cardPrice);
            cardBody.appendChild(cardCategory);

            card.appendChild(img);
            card.appendChild(cardBody);

            row.appendChild(card);
            locationProducts.appendChild(row);
        }
    } else {
        alert("No hay productos disponibles");
        location.reload();
    }
    return endIndex;
};

// Función para cargar más productos
const loadMoreProducts = () => {
    startIndex += itemPage;
    showProducts(loadedProducts, startIndex);
    if (startIndex >= loadedProducts.length) {
        allProductsRendered = true;
        loadMoreButton.style.display = "none";
    }
};

loadMoreButton.addEventListener("click", loadMoreProducts);

// Función para mapear productos con marcas y categorías
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

getProductsData()
    .then((data) => {
        const results = mapProducts(data.products, data.brands, data.categories);
        loadedProducts = results;
        showProducts(results, startIndex);
        saleSection(results);

        // Generar opciones de filtro por marca usando jQuery y Bootstrap
        const dropdownMenu = $('#brandsDropdownMenu');// Selección con jQuery
        data.brands.forEach(brand => {
            const option = $('<li>');
            const link = $('<a>');
            link.addClass('dropdown-item');
            link.attr('href', '#');
            link.text(brand.name);
            link.data('brandId', brand.id);
            link.on('click', function(event) {
                event.preventDefault();
                const brandId = $(this).data('brandId');
                if (brandId) {
                    const filteredProducts = results.filter(product => product.brand_id == brandId);
                    locationProducts.innerHTML = '';
                    loadMoreButton.style.display = "none";
                    const stockP = locationSale.querySelector('h3');
                    stockP.textContent = filteredProducts.length + " ARTICULOS";
                    showAllProducts(filteredProducts);
                }
            });
            option.append(link);
            dropdownMenu.append(option);
        });
        $('.dropdown-toggle').dropdown();
    })
    .catch((error) => {
        console.log(`El error es: ${error}`);
    });