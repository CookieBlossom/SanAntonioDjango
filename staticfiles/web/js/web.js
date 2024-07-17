import { getBrands, getCategories } from "./api.js";

const createCategories = (data) => {
    let location = document.getElementById("showCategories");
    data.forEach( element => {
        const divCol = document.createElement("div");
        divCol.classList.add("row"); 

        const card = document.createElement("div");
        card.classList.add("card");

        const title = document.createElement("h5");
        title.classList.add("card-title");
        title.textContent = `${element.name}`;

        card.appendChild(title);
        divCol.appendChild(card);
        location.appendChild(divCol);
    });
}

const createBrands = (data) => {
    const location = document.getElementById("showBrands");

    data.forEach(element => {
        const text = element.name;
        const image = element.image;
        const divCol = document.createElement("div");
        divCol.classList.add("row"); 

        const card = document.createElement("div");
        card.classList.add("card");

        const img = document.createElement("img");
        img.classList.add("card-img-top");
        img.src = `../media/${image}`;

        const cardBody = document.createElement("div");
        cardBody.classList.add("card-body")

        const cardTitle = document.createElement("h3");
        cardTitle.classList.add("card-title");
        cardTitle.textContent = text;
        
        card.appendChild(img);
        cardBody.appendChild(cardTitle);
        card.appendChild(cardBody);
        
        divCol.appendChild(card);
        location.appendChild(divCol);

        
    });
}

getBrands()
    .then((brands) => {
        createBrands(brands);
    })
    .catch((error)=> {
        console.log(`Èl error es: ${error}`);
    })    

getCategories()
.then((category) => {
    createCategories(category);
})
.catch((error)=> {
    console.log(`Èl error es: ${error}`);
})    