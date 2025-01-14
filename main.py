import sys
import zlib


text=b"""Lorem ipsum dolor sit amet, consectetur adipiscing elit. In pellentesque turpis vitae auctor vulputate. Fusce finibus imperdiet magna at aliquam. Nulla malesuada turpis tortor, sit amet ultrices leo tincidunt in. Vivamus libero quam, bibendum vel pharetra a, bibendum eu metus. Duis ac tortor diam. Maecenas ullamcorper in lorem et tempus. In a enim ut diam vehicula egestas nec vel nibh. Curabitur dapibus metus et diam tempor, quis pharetra dolor aliquet. Sed eu mattis lorem, ut auctor mauris. Donec fringilla vehicula tortor, sed molestie neque varius vel. Nulla sodales massa eu fringilla aliquam. Praesent ac velit malesuada, ultricies augue sed, sodales eros. Aenean ac turpis vehicula, vehicula odio at, placerat dui. Suspendisse ac diam urna. Mauris accumsan augue eget consectetur vehicula.

Nam dapibus sapien sem, vel tincidunt libero consequat et. Ut aliquam porta magna in sagittis. Integer a tempus ex, quis molestie massa. Nam venenatis ut velit at cursus. Sed elit quam, viverra in consectetur nec, consectetur in felis. Ut eget interdum urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Integer mattis feugiat commodo. Duis dignissim neque et mollis lacinia. Suspendisse quis finibus eros. Donec eget lacinia arcu.

Vestibulum et turpis placerat est ornare semper vel at tellus. Suspendisse mollis posuere neque, in vestibulum erat tincidunt nec. Mauris semper est libero, nec fermentum sapien hendrerit sed. Pellentesque convallis nunc ipsum, nec aliquet odio auctor vel. Donec rutrum, est ac pellentesque porta, est ante placerat ligula, non laoreet eros erat ac ipsum. Quisque volutpat in mauris in dictum. Integer efficitur lacus felis, id auctor neque posuere eget. Morbi fermentum ante ut orci dapibus, eu fringilla est volutpat.

Maecenas sit amet felis vitae diam commodo pretium a eu ligula. Fusce tincidunt, libero a congue tempor, enim lorem aliquet dolor, et efficitur ex lacus quis sapien. Praesent neque nisi, lobortis eu purus ac, lobortis maximus massa. Mauris ante purus, mattis vel lectus id, ullamcorper semper nisl. Suspendisse sit amet efficitur risus, et vulputate urna. Mauris tellus lectus, convallis a sollicitudin ac, tempor sed justo. Integer semper nibh lectus, vitae dapibus orci faucibus a. Aliquam iaculis, lorem sed porttitor fringilla, dolor ante pretium felis, non imperdiet odio dui eu tortor. Vivamus pharetra lectus non turpis luctus, sed aliquet mauris ornare. Nunc fermentum ullamcorper justo, quis molestie quam viverra sed.

Ut lobortis nec nulla nec tristique. Maecenas eu laoreet sem. Vestibulum dapibus volutpat nisl, nec tempor diam ullamcorper in. Praesent commodo dignissim malesuada. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aliquam posuere lacus non sodales tristique. Phasellus id mauris et risus rutrum tincidunt porta nec ex. Ut sed nunc venenatis, scelerisque velit quis, placerat nibh. Fusce finibus pretium urna, vel porta arcu. Integer lobortis dignissim quam vel placerat. In ultricies augue magna, id viverra nisi tempus eu. Pellentesque ut volutpat nisl. In in nisi diam. Phasellus convallis laoreet orci, sit amet dictum sem laoreet ut. Curabitur tortor neque, facilisis a turpis non, malesuada fermentum elit. Nam viverra in tellus faucibus scelerisque."""


text_size=sys.getsizeof(text)
print("\nsize of original text",text_size)

compressed = zlib.compress(text)

csize=sys.getsizeof(compressed)
print("\nsize of compressed text",csize)

decompressed=zlib.decompress(compressed)


dsize=sys.getsizeof(decompressed)
print("\nsize of decompressed text",dsize)

print("\nDifference of size= ", text_size-csize)
