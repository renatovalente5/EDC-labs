<root> {
for $l in distinct-values(collection('cursos')//local)
(:let $a := collection("cursos")//curso
for $l in distinct-values($a/local) :)
return
  <elem>{$l}</elem>
} </root>