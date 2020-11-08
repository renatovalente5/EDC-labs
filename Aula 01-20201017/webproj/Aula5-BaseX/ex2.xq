module namespace funcs = "com.funcs.my.index";

declare updating function funcs:inserirCurso($aguid)
{
  let $cs := collection("cursos")//cursos
  return insert node <curso><guid>{$aguid}</guid></curso> as first into $cs
};


