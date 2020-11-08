<root>
  {
     let $areaCientifica := "Informática"
     for $c in collection('cursos')//curso
     where $c//areacientifica = $areaCientifica
     return 
       <elem>
          { $c/nome }
       </elem>
   }
</root>