let $cd := collection("cursos")//curso
for $c in $cd where $c//guid = "54" 
return replace node $c/ciclo/text() with '10'
