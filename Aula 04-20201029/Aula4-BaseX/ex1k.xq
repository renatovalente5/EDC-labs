<root>{
   for $l in distinct-values(collection('cursos')//local)
   return 
   
     <elem>
       <local>{ $l }</local>
       {
        for $c in collection('cursos')//curso[local/text() = $l]
        (: for $c in collection('cursos')//curso :)    (:Alternativas:)
        (: where $c//local = $l :)
        return 
          <curso>{ $c/nome/text() }</curso>
          (: <curso>{ $c/nome }</curso> :)
        }
     </elem>
   }
</root>