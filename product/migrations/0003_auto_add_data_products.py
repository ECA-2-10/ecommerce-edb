# Generated by Django 5.1.3 on 2024-11-19 14:30

from django.db import migrations

def add_initial_products(apps, schema_editor):
    # Add initial product/images to the database
    Product = apps.get_model('product', 'Product')
    Department = apps.get_model('product', 'Department')
    Category = apps.get_model('product', 'Category')
    todos_productos = []

    # Obtener los departamentos y categorías existentes
    cocina = Department.objects.get(name='Cocina')
    # Categorías de Cocina
    electrodomesticos = Category.objects.get(department=cocina, name='Electrodomesticos')
    utensilios = Category.objects.get(department=cocina, name='Utensilios de Cocina')
    peque_electro = Category.objects.get(department=cocina, name='Pequeños Electrodomésticos')
    almacenamiento = Category.objects.get(department=cocina, name='Almacenamiento de Alimentos')
    otros = Category.objects.get(department=cocina, name='Otros')

    # Productos de Cocina
    prod_cocina = [
        ('Refrigerador Samsung Family Hub','Refrigerador inteligente con pantalla táctil y conectividad Wi-Fi.',2499.99,'product/images/refrigerador_samsung_family_hub.jpg','Samsung',30,electrodomesticos),    
        ('Lavavajillas Bosch Serie 6','Lavavajillas eficiente con múltiples programas de lavado.',899.99,'product/images/lavavajillas_bosch_serie6.jpg','Bosch',20,electrodomesticos),    
        ('Horno Microondas LG NeoChef','Microondas con tecnología inverter para cocción uniforme.',299.99,'product/images/microondas_lg_neochef.jpg','LG',0,electrodomesticos),    
        ('Placa de Inducción Teka IIC','Placa de inducción de 4 zonas con controles táctiles.',499.99,'product/images/placa_induccion_teka_iic.jpg','Teka',25,electrodomesticos),    
        ('Extractor de Aire Siemens iQ700','Extractor de aire silencioso con sensor de humedad.',399.99,'product/images/extractor_aire_siemens_iq700.jpg','Siemens',15,electrodomesticos),    

        ('Juego de Cuchillos Global 8 Piezas','Set de cuchillos japoneses de alta calidad para cocina profesional.',149.99,'product/images/cuchillos_global_8piezas.jpg','Global',100,utensilios),    
        ('Sartenes Tefal Titanium','Juego de sartenes antiadherentes con tecnología Titanium.',129.99,'product/images/sartenes_tefal_titanium.jpg','Tefal',80,utensilios),    
        ('Set de Ollas Le Creuset','Juego de ollas de hierro fundido esmaltado de alta calidad.',599.99,'product/images/ollas_lecreuset.jpg','Le Creuset',0,utensilios),    
        ('Batidora KitchenAid Artisan','Batidora de pie con múltiples accesorios y colores disponibles.',349.99,'product/images/batidora_kitchenaid_artisan.jpg','KitchenAid',60,utensilios),    
        ('Tabla de Cortar de Bambú','Tabla de cortar ecológica y resistente para todo tipo de alimentos.',29.99,'product/images/tabla_cortar_bambu.jpg','OXO',150,utensilios),    

        ('Tostadora Philips Daily Collection','Tostadora con 6 niveles de tostado y funciones de descongelado.',49.99,'product/images/tostadora_philips_daily.jpg','Philips',70,peque_electro),    
        ('Cafetera Nespresso Vertuo','Cafetera cápsulas con tecnología de centrifusión para café y espresso.',199.99,'product/images/cafetera_nespresso_vertuo.jpg','Nespresso',55,peque_electro),    
        ('Licuadora Vitamix 5200','Licuadora de alto rendimiento para smoothies y batidos.',449.99,'product/images/licuadora_vitamix_5200.jpg','Vitamix',35,peque_electro),    
        ('Freidora de Aire Philips','Freidora de aire saludable con tecnología Rapid Air.',299.99,'product/images/freidora_aire_philips.jpg','Philips',45,peque_electro),    
        ('Robot de Cocina Moulinex Companion','Robot multifunción para picar, cocinar y amasar.',599.99,'product/images/robot_cocina_moulinex_companion.jpg','Moulinex',25,peque_electro),    
        ('Cafetera Espresso DeLonghi Magnifica','Máquina de café espresso automática con molinillo integrado.',699.99,'product/images/cafetera_delonghi_magnifica.jpg','DeLonghi',20,peque_electro),    
        ('Plancha para Panini Breville','Plancha eléctrica para paninis y sándwiches con placas antiadherentes.',89.99,'product/images/plancha_panini_breville.jpg','Breville',65,peque_electro),    
        ('Extractor de Jugos Omega J8006','Extractor de jugos de alta eficiencia para jugos fríos.',349.99,'product/images/extractor_jugos_omega_j8006.jpg','Omega',30,peque_electro),    
        ('Máquina de Hacer Pan Panasonic SD-YD250','Máquina automática para hacer pan con múltiples programas.',199.99,'product/images/maquina_pan_panasonic_sdyd250.jpg','Panasonic',40,peque_electro),    
        ('Humidificador Philips Series 2000','Humidificador ultrasónico con control de humedad y apagado automático.',129.99,'product/images/humidificador_philips_series2000.jpg','Philips',50,peque_electro),    
        ('Ventilador de Escritorio Honeywell HT-900E','Ventilador compacto y silencioso para uso en cocina.',39.99,'product/images/ventilador_honeywell_ht900e.jpg','Honeywell',100,peque_electro),    
        ('Calentador de Agua Instantáneo Ariston','Calentador de agua sin depósito con rápida provisión de agua caliente.',299.99,'product/images/calentador_agua_ariston.jpg','Ariston',20,peque_electro),    

        ('Despensa Inteligente SmartStor','Sistema de almacenamiento modular con sensores de temperatura.',499.99,'product/images/despensa_inteligente_smartstor.jpg','SmartStor',10,almacenamiento),    
        ('Contenedores Herméticos Lock&Lock','Juego de 20 contenedores plásticos con cierre hermético.',59.99,'product/images/contenedores_locklock.jpg','Lock&Lock',200,almacenamiento),    
        ('Envasadora al Vacío FoodSaver V4840','Máquina de envasado al vacío con múltiples modos de sellado.',199.99,'product/images/envasadora_foodsaver_v4840.jpg','FoodSaver',35,almacenamiento),    
        ('Refrigerador de Vino Vinotemp 24 Botellas','Refrigerador especializado para almacenamiento de vinos con control de temperatura.',799.99,'product/images/refrigerador_vinotemp_24botellas.jpg','Vinotemp',15,almacenamiento),    

        ('Máquina de Hacer Café Moka','Máquina de café tradicional italiana para preparar moka pot.',49.99,'product/images/maquina_cafe_moka.jpg','Bialetti',80,otros),    
        ('Set de Medidores de Cocina OXO','Juego de medidores de cocina en acero inoxidable con imán.',39.99,'product/images/medidores_oxo.jpg','OXO',120,otros)
    ]

    # Añadir productos de Cocina
    todos_productos.extend(prod_cocina)

    # --------------------- Añadir Productos para Electrónica ---------------------

    # Obtener el departamento de Electrónica
    electronica = Department.objects.get(name='Electrónica')

    # Obtener las categorías de Electrónica
    audio_sonido = Category.objects.get(department=electronica, name='Audio y Sonido')
    televisores_video = Category.objects.get(department=electronica, name='Televisores y Video')

    # Productos para Audio y Sonido
    prod_audio_sonido = [
        ('Bose SoundLink Revolve','Altavoz portátil con sonido envolvente de 360 grados.',199.99,'product/images/bose_soundlink_revolve.jpg','Bose',50,audio_sonido),
        ('Sony WH-1000XM4','Auriculares inalámbricos con cancelación de ruido líder en la industria.',349.99,'product/images/sony_wh1000xm4.jpg','Sony',75,audio_sonido),
        ('Sonos One (Gen 2)','Altavoz inteligente con integración de Alexa y Google Assistant.',199.99,'product/images/sonos_one_gen2.jpg','Sonos',60,audio_sonido)
    ]

    # Productos para Televisores y Video
    prod_televisores_video = [
        ('Samsung QLED Q90T','Televisor QLED 4K con tecnología de imagen avanzada.',1499.99,'product/images/samsung_qled_q90t.jpg','Samsung',20,televisores_video),
        ('LG OLED CX','Televisor OLED 4K con negros perfectos y colores vibrantes.',1799.99,'product/images/lg_oled_cx.jpg','LG',15,televisores_video),
        ('Sony Bravia X90J','Televisor LED 4K con procesador de imagen avanzado.',1299.99,'product/images/sony_bravia_x90j.jpg','Sony',25,televisores_video)
    ]

    todos_productos.extend(prod_audio_sonido)
    todos_productos.extend(prod_televisores_video)

    # --------------------- Añadir Productos para Hogar ---------------------

    # Obtener el departamento de Hogar
    hogar = Department.objects.get(name='Hogar')

    # Obtener las categorías de Hogar
    muebles = Category.objects.get(department=hogar, name='Muebles')
    decoracion = Category.objects.get(department=hogar, name='Decoración')

    # Productos para Muebles
    prod_muebles = [
        ('Sofá Seccional IKEA VIMLE','Sofá modular de alta calidad con múltiples configuraciones.',899.99,'product/images/sofa_vimle.jpg','IKEA',10,muebles),
        ('Mesa de Comedor Pottery Barn','Mesa de comedor de madera maciza con capacidad para 8 personas.',799.99,'product/images/mesa_pottery_barn.jpg','Pottery Barn',5,muebles),
        ('Cama King Size Zinus','Cama de madera con diseño moderno y estructura resistente.',499.99,'product/images/cama_king_zinus.jpg','Zinus',20,muebles)
    ]

    # Productos para Decoración
    prod_decoracion = [
        ('Lámpara de Techo Philips Hue','Lámpara inteligente con control de color y brillo vía app.',199.99,'product/images/lampara_philips_hue.jpg','Philips',30,decoracion),
        ('Cuadro Abstracto Moderno','Obra de arte abstracta en lienzo para decoración de interiores.',149.99,'product/images/cuadro_abstracto_moderno.jpg','Artistry',25,decoracion),
        ('Alfombra Oriental Safavieh','Alfombra de diseño oriental con materiales de alta calidad.',299.99,'product/images/alfombra_safavieh.jpg','Safavieh',10,decoracion)
    ]

    todos_productos.extend(prod_muebles)
    todos_productos.extend(prod_decoracion)

    # --------------------- Añadir Productos para Jardinería ---------------------

    # Obtener el departamento de Jardinería
    jardin = Department.objects.get(name='Jardinería')

    # Obtener las categorías de Jardinería
    herramientas_jardin = Category.objects.get(department=jardin, name='Herramientas de Jardín')

    # Productos para Herramientas de Jardín
    prod_herramientas_jardin = [
        ('Juego de Herramientas Fiskars','Set completo de herramientas de jardín ergonómicas.',89.99,'product/images/herramientas_fiskars.jpg','Fiskars',40,herramientas_jardin),
        ('Motosierra Stihl MS 271','Motosierra profesional con alta eficiencia y durabilidad.',399.99,'product/images/motosierra_stihl_ms271.jpg','Stihl',10,herramientas_jardin),
        ('Regadera de Hierro Forjada','Regadera decorativa y funcional para jardines.',29.99,'product/images/regadera_hierro_forgada.jpg','GardenPro',100,herramientas_jardin)
    ]

    todos_productos.extend(prod_herramientas_jardin)

    # --------------------- Añadir Productos para Deportes ---------------------

    # Obtener el departamento de Deportes
    deportes = Department.objects.get(name='Deportes')

    # Obtener las categorías de Deportes
    fitness = Category.objects.get(department=deportes, name='Fitness')
    outdoor = Category.objects.get(department=deportes, name='Outdoor')

    # Productos para Fitness
    prod_fitness = [
        ('Bicicleta Estática Peloton','Bicicleta estática con pantalla interactiva para clases en vivo.',1899.99,'product/images/bicicleta_peloton.jpg','Peloton',15,fitness),
        ('Mancuernas Ajustables Bowflex','Set de mancuernas ajustables para entrenamiento en casa.',199.99,'product/images/mancuernas_bowflex.jpg','Bowflex',40,fitness),
        ('Colchoneta de Yoga Liforme','Colchoneta antideslizante con alineación visual para yoga.',99.99,'product/images/colchoneta_liforme.jpg','Liforme',60,fitness)
    ]

    # Productos para Outdoor
    prod_outdoor = [
        ('Tienda de Campaña Coleman','Tienda de campaña resistente para 4 personas.',149.99,'product/images/tienda_campaña_coleman.jpg','Coleman',25,outdoor),
        ('Mochila de Senderismo Osprey','Mochila ergonómica con múltiples compartimentos y soporte lumbar.',129.99,'product/images/mochila_osprey.jpg','Osprey',30,outdoor),
        ('Saco de Dormir The North Face','Saco de dormir ligero y cálido para condiciones frías.',199.99,'product/images/saco_dormir_nf.jpg','The North Face',20,outdoor)
    ]

    todos_productos.extend(prod_fitness)
    todos_productos.extend(prod_outdoor)

    # --------------------- Añadir Productos para Oficina ---------------------

    # Obtener el departamento de Oficina
    oficina = Department.objects.get(name='Oficina')

    # Obtener las categorías de Oficina
    equipos_oficina = Category.objects.get(department=oficina, name='Equipos de Oficina')
    suministros = Category.objects.get(department=oficina, name='Suministros')

    # Productos para Equipos de Oficina
    prod_equipos_oficina = [
        ('Impresora HP LaserJet Pro','Impresora láser multifunción con conectividad Wi-Fi.',299.99,'product/images/impresora_hp_ljpro.jpg','HP',40,equipos_oficina),
        ('Escritorio Ajustable FlexiSpot','Escritorio de altura ajustable eléctrico para ergonomía.',399.99,'product/images/escritorio_flexispot.jpg','FlexiSpot',25,equipos_oficina),
        ('Silla Ergonomica Herman Miller Aeron','Silla de oficina ergonómica con soporte lumbar avanzado.',1199.99,'product/images/silla_aeron.jpg','Herman Miller',10,equipos_oficina)
    ]

    # Productos para Suministros
    prod_suministros = [
        ('Paquete de Bolígrafos Bic','Set de 12 bolígrafos de tinta azul.',9.99,'product/images/boligrafos_bic.jpg','Bic',500,suministros),
        ('Cuadernos Moleskine','Cuaderno de tapa dura con papel de alta calidad.',19.99,'product/images/cuaderno_moleskine.jpg','Moleskine',300,suministros),
        ('Organizador de Escritorio AmazonBasics','Organizador de escritorio con múltiples compartimentos.',24.99,'product/images/organizador_amazonbasics.jpg','AmazonBasics',150,suministros)
    ]

    todos_productos.extend(prod_equipos_oficina)
    todos_productos.extend(prod_suministros)

    # --------------------- Añadir Productos para Salud ---------------------

    # Obtener el departamento de Salud
    salud = Department.objects.get(name='Salud')

    # Obtener las categorías de Salud
    equipos_medicos = Category.objects.get(department=salud, name='Equipos Médicos')

    # Productos para Equipos Médicos
    prod_equipos_medicos = [
        ('Monitor de Presión Omron','Monitor digital para medir la presión arterial en casa.',49.99,'product/images/monitor_presion_omron.jpg','Omron',150,equipos_medicos),
        ('Termómetro Digital Braun','Termómetro digital rápido y preciso para uso doméstico.',19.99,'product/images/termometro_braun.jpg','Braun',200,equipos_medicos),
        ('Oxímetro de Pulso Zacurate','Oxímetro portátil para medir saturación de oxígeno y pulso.',29.99,'product/images/oximetro_zacurate.jpg','Zacurate',120,equipos_medicos)
    ]

    todos_productos.extend(prod_equipos_medicos)

    # Añadir todos los productos a la base de datos
    for name, description, price, image, maker, stock, category in todos_productos:
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            image=image,
            maker=maker,
            stock=stock,
            category=category
        )

class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_add_data_categories'),
    ]

    operations = [
        migrations.RunPython(add_initial_products)
    ]
