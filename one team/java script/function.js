function greet (){
    console.log("hello");
}
greet();



parameters--->

function greet (name){
    console.log("hello "+name+"!")

}
greet("abhay");
greet("nithin");


function greet(name,age){
    console.log(`your name is ${name} and your age is ${age}`)
}
greet("abhin",22)
greet("hari",22)
greet("jayathri",22)


function prime(number){
    if (number<=1){
         console.log(" not prime");
         return;}

    if(number==2){

     console.log("prime");
     return;}

    if(number %2 ===0){
        console.log(" not prime")
        return;}

for(let i=3;i<=number/2;i+=2){
    if(number%i===0){
        console.log("not prime");
        return;
    }
}
console.log("is prime")
       
}
prime(7);
prime(10)
prime(131)
prime(12)
prime(102)
prime(103)
prime(100)