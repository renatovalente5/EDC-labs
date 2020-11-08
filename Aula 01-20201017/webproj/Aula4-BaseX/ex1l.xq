<root>{
   for $d in distinct-values(collection('cursos')//departamento)
   return 
   
     <elem>
       <departamento>{ $d }</departamento>
       {
        for $c in collection('cursos')//curso
        where $c//departamento = $d
        return 
          <curso>{ $c/nome/text() }</curso>
        }
     </elem>
   }
</root>