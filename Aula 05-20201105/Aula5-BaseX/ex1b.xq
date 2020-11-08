let $cd := collection("cursos")//curso
for $c in $cd where $c//guid = "0011" 
return delete node $c
