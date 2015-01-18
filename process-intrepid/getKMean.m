 
data = load('..\data\ANL-Intrepid-2009-1.swf\processTime.txt');
[idx, c] = kmeans(data, 12);
hist(idx)