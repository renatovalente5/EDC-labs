<root>{
  for $d in distinct-values(collection('cursos')//areascientificas)
  return 
  <elem>
    {$d}
  </elem>
}</root>