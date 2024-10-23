const tableRoot = document.querySelector("#csvRoot");
const csvFileInput = document.querySelector("#csvFileInput");
const tableCsv = new TableCsv(tableRoot);

csvFileInput.addEventListener("change", e => {
    Papa.parse(csvFileInput.files[0], {
        delimiter: ",",          // Delimitador para el archivo CSV
        skipEmptyLines: true,     // Saltar líneas vacías
        complete: results => {
            // Actualizar la tabla con los datos parseados
            tableCsv.update(results.data.slice(1), results.data[0]);
        }
    });
});