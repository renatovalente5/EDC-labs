<root>{
   for $a in distinct-values(collection('cursos')//areacientifica)
   return 
   
     <elem>
       <areacientifica>{ $a }</areacientifica>
       {
        for $c in collection('cursos')//curso
        where $c//areacientifica = $a
        return 
          <curso>{ $c/nome/text() }</curso>
        }
     </elem>
   }
</root>