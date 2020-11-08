<root>
  {
     let $guid := "15"
     for $d in collection('cursos')//curso
     where $d/guid = $guid
     return 
       <elem>
          { $d/guid, $d/nome, $d/grau, $d/local }
       </elem>
   }
</root>