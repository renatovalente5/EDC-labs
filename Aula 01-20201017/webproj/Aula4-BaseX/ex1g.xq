<root>
  {
     let $departamento := "Departamento de Biologia"
     for $d in collection('cursos')//curso
     where $d//departamento = $departamento
     return 
       <elem>
          { $d//nome }
       </elem>
   }
</root>