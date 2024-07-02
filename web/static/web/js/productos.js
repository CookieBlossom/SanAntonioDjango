import { getProductsData } from "./api.js";


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
    console.log(data);
    console.log(mapProducts(data.products, data.brands, data.categories));
})
.catch((error)=> {
    console.log(`Èl error es: ${error}`);
})    