(*two sum problem*)
type Res = (int*int list);
type Index = (int*int) list;

(*the following is a helper function to get the item from a list*)
let rec ElementRetrieve (numList:int list)(lengthOfList:int):int = 
  match numList with
  | [] -> -1;
  |hd::tl -> if lengthOfList=0 then hd else ElementRetrieve tl lengthOfList-1;
;;
(*helper function to retrieve*)
let TwoSum (nums:int list)(target:int):int list =
  (*creating a mutable variable using `ref`*)
  let compliment = ref 0 in
  (*creating a mutable dictionary using ref*)
  let indices:Index = ref {} in
  let numLen = List.length nums in (*length of the list*)
  
  for i = 0 to numLen () do
    compliment = target - ElementRetrieve (nums)(i)

  done
;;