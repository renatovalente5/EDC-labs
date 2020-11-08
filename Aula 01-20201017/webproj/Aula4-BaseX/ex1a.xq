<root> {
for $a in collection("cursos")//curso
return
  <elem>
    {$a/guid}
    {$a/nome}
  </elem>
} </root>
