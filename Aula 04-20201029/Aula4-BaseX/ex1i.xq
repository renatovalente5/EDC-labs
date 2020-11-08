<root>
  {
     let $depart := "Departamento de Biologia"
     for $d in collection('cursos')//curso
     where $d//departamento = $depart
     return 
       <elem>
          { $d/nome }
       </elem>
   }
</root>