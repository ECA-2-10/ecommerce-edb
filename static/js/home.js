function updateURLWithDepartment(selectElement) {
    const departmentName = selectElement.value;
    filterCategoriesByDepartment(departmentName);
    const url = new URL(window.location.href);
    if (departmentName === 'Todos los departamentos') {
        url.searchParams.delete('department');
    } else {
        url.searchParams.set('department', departmentName);
    }
    url.searchParams.delete('category'); // Reset category when department changes
    window.history.pushState({}, '', url);
    filterProducts();
}

function filterProductsByCategory(categoryName) {
    const url = new URL(window.location.href);
    if (categoryName === 'Todas las categorías') {
        url.searchParams.delete('category');
    } else {
        url.searchParams.set('category', categoryName);
    }
    window.history.pushState({}, '', url);
    filterProducts();
}

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

document.addEventListener('DOMContentLoaded', (event) => {
    const urlParams = new URLSearchParams(window.location.search);
    const department = urlParams.get('department');
    const category = urlParams.get('category');
    const searchQuery = urlParams.get('search');

    if (department) {
        document.getElementById('departmentSelect').value = department;
        filterCategoriesByDepartment(department);
    }

    if (category) {
        filterProductsByCategory(category);
    }

    if (searchQuery) {
        document.getElementById('searchInput').value = searchQuery;
    }

    filterProducts();
    updateScrollButtonsVisibility();
});

function filterCategoriesByDepartment(departmentName) {
    // Actualiza la visibilidad de los botones de categoría en el header
    const categoryButtons = document.querySelectorAll('.category-button');
    categoryButtons.forEach(button => {
        if (departmentName === "Todos los departamentos" || button.getAttribute('data-department') === departmentName) {
            button.style.display = "inline-flex";
        } else {
            button.style.display = "none";
        }
    });
    updateScrollButtonsVisibility();
}

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

        if (category && category !== "Todas las categorías" && productCategory !== category) {
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

document.getElementById('categoriesContainer').addEventListener('scroll', updateScrollButtonsVisibility);