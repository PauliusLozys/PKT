-- https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=6&page=show_problem&problem=379

import Data.Char
import Data.String
import System.IO
import Text.Printf (printf)

calculate :: [Double] -> Double 
calculate x = do
  let x1 = [x !! 0, x !! 1]
  let x2 = [x !! 2, x !! 3]
  let x3 = [x !! 4, x !! 5]

  let a = ((x1 !! 1)**2 + (x1 !! 0)**2 - (x3 !! 1)**2 - (x3 !! 0)**2 -((x1 !! 1)-(x3 !! 1)) * ((x1 !! 1)**2 + (x1 !! 0)**2 - (x2 !! 1)**2 - (x2 !! 0)**2) / ((x1 !! 1)-(x2 !! 1))) / 2 / ((x1 !! 0)-(x3 !! 0)-((x1 !! 1)-(x3 !! 1))*((x1 !! 0)-(x2 !! 0))/((x1 !! 1)-(x2 !! 1)))
  let b = ((x1 !! 1)**2 + (x1 !! 0)**2 - (x2 !! 1)**2 - (x2 !! 0)**2 - 2*a * ((x1 !! 0)-(x2 !! 0))) / ((x1 !! 1)-(x2 !! 1)) / 2
  
  let circumference = sqrt ((a - (x1 !! 0))**2 + (b - (x1 !! 1))**2) * 2 * pi
  circumference

main :: IO ()
main = do

  file <- openFile "data.txt" ReadMode
  contents <- hGetContents file
  let splitContent = lines contents
  let bazinga = [words x | x <- splitContent]
  let convertedToDoubles = [[read s :: Double | s <- x] | x <- bazinga]
  let final = [calculate x | x <- convertedToDoubles]

  appendFile "output.txt" $concat [printf "%.2f\n" x | x <- final]
  hClose file
  print "Done"
