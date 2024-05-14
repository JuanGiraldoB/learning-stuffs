<?php
    const API_URL = "https://whenisthenextmcufilm.com/api";

    # Inicializar sesion de cURL; ch = cURL handle
    $ch = curl_init(API_URL);

    // Indicar que no muestre resultado en pantalla
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    // ejecutar la peticion y guardar el resultado
    $result = curl_exec($ch);

    $data = json_decode($result, true);
    curl_close($ch);
    var_dump($data);

?>

<main>
    <h2>La proxima pelicula de marvel</h2>
</main>


<style>
    :root {
        color-scheme: light dark;
    }

    body {
        display: grid;
        place-content: center;
    }
</style>