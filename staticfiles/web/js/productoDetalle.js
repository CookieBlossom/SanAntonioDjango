import { getProductsData, getSizes } from "./api.js";
const url = window.location.href;
const productId = url.match(/\/detalle-producto\/(\d+)\//)[1];
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
    const loadInformation = ( results = [], sizes = [] ) => {
        // const sizes = results.sizes;
        const name = results.name;
        const price = results.price;
        const brand = results.brand_name;
        const stock = results.quantity;
        const row = document.createElement("div");
        row.classList.add("row");
        const col = document.createElement("div");
        col.classList.add("col");
        const image = document.createElement("img");
        image.src = `../media/${results.image}`;
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
        colBody.appendChild(title);
        colBody.appendChild(productInfo);
        colBody.appendChild(selecterInfo);

        locationInfoProduct.appendChild(col);
        locationInfoProduct.appendChild(colBody);
        }


    getProductsData()
        .then((data) => {
            const results = mapProducts(data.products, data.brands, data.categories);
            const product = results[productId-1];
            console.log(product);
            getSizes()
                .then((sizes) => {
                    console.log(sizes);
                    loadInformation(product, sizes);
                })
                .catch((error) => {

                });
            
        })
        .catch((error) => {
            console.log(`El error es: ${error}`);
        });
} else {
    console.error('No se pudo obtener el ID del producto desde la URL');
}

