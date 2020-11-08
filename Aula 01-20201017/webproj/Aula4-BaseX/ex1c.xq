<root>{
  for $d in distinct-values(collection('cursos')//departamento)
  return 
  <elem>
    {$d}
  </elem>
}</root>