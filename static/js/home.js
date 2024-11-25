// Función para actualizar la URL cuando se selecciona un departamento
function updateURLWithDepartment(selectElement) {
    const departmentName = selectElement.value;
    const url = new URL(window.location.href);

    if (departmentName === 'Todos los departamentos') {
        url.searchParams.delete('department');
    } else {
        url.searchParams.set('department', departmentName);
    }

    url.searchParams.delete('category'); // Resetear categoría cuando cambia el departamento
    window.history.pushState({}, '', url);

    filterCategoriesByDepartment(departmentName);
    filterProducts();
}

// Función para filtrar productos por categoría
function filterProductsByCategory(categoryName) {
    const url = new URL(window.location.href);
    const allButton = document.querySelector('.category-button.all-button');
    const currentDepartment = allButton.getAttribute('data-department') || '';

    if (!categoryName) { // Si categoryName está vacío, es el botón "Todos"
        url.searchParams.delete('category');
    } else {
        url.searchParams.set('category', categoryName);
    }

    window.history.pushState({}, '', url);
    filterProducts();

    // Manejar la clase 'active' en los botones de categoría
    const categoryButtons = document.querySelectorAll('.category-button');
    categoryButtons.forEach(button => {
        const btnCategory = button.getAttribute('data-category-name');
        if (btnCategory === categoryName) {
            button.classList.add('active');
        } else {
            button.classList.remove('active');
        }
    });

    if (!categoryName) {
        // Si se selecciona "Todos", activar el botón "Todos"
        if (allButton) {
            allButton.classList.add('active');
        }
    } else {
        // Asegurar que "Todos" no está activo
        if (allButton) {
            allButton.classList.remove('active');
        }
    }
}

// Funciones para manejar la búsqueda
function handleSearch(event) {
    if (event.key === 'Enter') {
        performSearch(event.target.value);
    }
}

function triggerSearch() {
    const searchQuery = document.getElementById('searchInput').value;
    performSearch(searchQuery);
}

function performSearch(searchQuery) {
    const url = new URL(window.location.href);
    if (searchQuery.trim() === '') {
        url.searchParams.delete('search');
    } else {
        url.searchParams.set('search', searchQuery);
    }
    window.history.pushState({}, '', url);
    filterProducts();
}

// Evento al cargar el DOM
document.addEventListener('DOMContentLoaded', (event) => {
    const urlParams = new URLSearchParams(window.location.search);
    const department = urlParams.get('department');
    const category = urlParams.get('category');
    const searchQuery = urlParams.get('search');

    if (department) {
        document.getElementById('departmentSelect').value = department;
        filterCategoriesByDepartment(department);
    } else {
        // Mostrar todas las categorías si no hay departamento seleccionado
        filterCategoriesByDepartment('Todos los departamentos');
    }

    if (category) {
        filterProductsByCategory(category);
    } else {
        // Asegurarse de que el botón "Todos" esté seleccionado visualmente
        const allButton = document.querySelector('.category-button.all-button');
        if (allButton) {
            allButton.classList.add('active');
        }
    }

    if (searchQuery) {
        document.getElementById('searchInput').value = searchQuery;
    }

    filterProducts();
    updateScrollButtonsVisibility();
});

// Función para filtrar las categorías según el departamento
function filterCategoriesByDepartment(departmentName) {
    const categoryButtons = document.querySelectorAll('.category-button');
    categoryButtons.forEach(button => {
        if (button.classList.contains('all-button')) {
            // Siempre mostrar el botón "Todos"
            button.style.display = "inline-flex";
        } else {
            const btnDepartment = button.getAttribute('data-department');
            if (departmentName === "Todos los departamentos" || btnDepartment === departmentName) {
                // Mostrar botón si pertenece al departamento seleccionado o si se muestran todos los departamentos
                button.style.display = "inline-flex";
            } else {
                // Ocultar botón si no pertenece al departamento seleccionado
                button.style.display = "none";
            }
        }
    });
    updateScrollButtonsVisibility();
}

// Función para filtrar los productos según los filtros aplicados
function filterProducts() {
    const urlParams = new URLSearchParams(window.location.search);
    const department = urlParams.get('department');
    const category = urlParams.get('category');
    const searchQuery = urlParams.get('search') ? urlParams.get('search').toLowerCase() : '';

    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => {
        const productDepartment = card.getAttribute('data-department');
        const productCategory = card.getAttribute('data-category');
        const productName = card.getAttribute('data-name').toLowerCase();

        let isVisible = true;

        if (department && department !== "Todos los departamentos" && productDepartment !== department) {
            isVisible = false;
        }

        if (category && productCategory !== category) { // Simplificado ya que category es eliminado si es "Todos"
            isVisible = false;
        }

        if (searchQuery && !productName.includes(searchQuery)) {
            isVisible = false;
        }

        if (isVisible) {
            card.classList.remove('d-none');
        } else {
            card.classList.add('d-none');
        }
    });
}

// Funciones para manejar el desplazamiento de categorías
function scrollCategories(scrollAmount) {
    const container = document.getElementById('categoriesContainer');
    container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    setTimeout(updateScrollButtonsVisibility, 300); // Asegura que la visibilidad se actualice después de que finalice el desplazamiento
}

function updateScrollButtonsVisibility() {
    const container = document.getElementById('categoriesContainer');
    const scrollLeftButton = document.getElementById('scrollLeft');
    const scrollRightButton = document.getElementById('scrollRight');

    if (container.scrollLeft > 0) {
        scrollLeftButton.classList.add('show');
    } else {
        scrollLeftButton.classList.remove('show');
    }

    if (container.scrollWidth > container.clientWidth && container.scrollLeft + container.clientWidth < container.scrollWidth - 1) {
        // El '-1' es para manejar posibles discrepancias de redondeo
        scrollRightButton.classList.add('show');
    } else {
        scrollRightButton.classList.remove('show');
    }
}

// Evento para actualizar la visibilidad de los botones de desplazamiento al hacer scroll
document.getElementById('categoriesContainer').addEventListener('scroll', updateScrollButtonsVisibility);
