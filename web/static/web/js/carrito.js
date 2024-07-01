function agregarAlCarrito(productoId) {
    var cantidadSeleccionada = document.getElementById('cantidadSeleccionada').value;
    $.ajax({
        type: 'POST',
        url: '/agregar-al-carrito/',  // Ruta donde manejas la lógica en Django
        data: {
            producto_id: productoId,
            cantidad: cantidadSeleccionada
        },
        success: function(response) {
            // Manejar la respuesta del servidor si es necesario
            console.log('Producto agregado al carrito con éxito');
        },
        error: function(error) {
            // Manejar errores si ocurren
            console.error('Error al agregar producto al carrito:', error);
        }
    });
}