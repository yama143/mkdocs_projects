var table = document.getElementById('table-id');
var sort = new Tablesort(table);

table.addEventListener('beforeSort', function() {
  alert('Table is about to be sorted!');
});

table.addEventListener('afterSort', function() {
  alert('Table sorted!');
});  