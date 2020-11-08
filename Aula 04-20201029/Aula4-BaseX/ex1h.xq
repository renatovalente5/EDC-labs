<root>
  {
     let $local := "Campus Universitário de Santiago, Aveiro"
     for $l in collection('cursos')//curso[local=$local]
     (:where $l//local = $local:)
     return 
       <elem>
          { $l/nome/text() }
       </elem>
   }
</root>