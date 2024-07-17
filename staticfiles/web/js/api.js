let API_BASE_URL = "http://127.0.0.1:8000" // URL de la API para entorno de desarrollo local

if (window.location.hostname === "sanantoniodjango.onrender.com") {
    // URL de la API para entorno de producción (Render)
    API_BASE_URL = "https://sanantoniodjango.onrender.com";
}


export const getProducts = async() => {
    try{

        const response = await fetch(`${API_BASE_URL}/web/api/products/`);
        const data = await response.json();

        return data;
    }catch(error){
        console.log(`El error es: ${error}`);
    }

}

export const getBrands = async() => {
    try{

        const response = await fetch(`${API_BASE_URL}/web/api/brands/`);
        const data = await response.json();

        return data;
    }catch(error){
        console.log(`El error es: ${error}`);
    }

}

export const getCategories = async() => {
    try{

        const response = await fetch(`${API_BASE_URL}/web/api/categories/`);
        const data = await response.json();

        return data;
    }catch(error){
        console.log(`El error es: ${error}`);
    }

}

export const getSizes = async() => {
    try{

        const response = await fetch(`${API_BASE_URL}/web/api/sizes/`);
        const data = await response.json();

        return data;
    }catch(error){
        console.log(`El error es: ${error}`);
    }

}

export const getProductsData = async() => {
    try{

        const response = await fetch(`${API_BASE_URL}/web/api/productsData/`);
        const data = await response.json();

        return data;
    }catch(error){
        console.log(`El error es: ${error}`);
    }

}