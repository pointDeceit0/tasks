fun intersection(first: IntArray, second: IntArray): List<Int> {
    // Given two arrays
    // return them intersection
    var first = first.toHashSet()
    var second = second.toHashSet()

    var ind1 = 0
    var ind2 = 0
    //var len: Int = max(first.length, second.length)

    var ans = mutableListOf<Int>()

    for (el in first) {
        if (second.contains(el)) {
            val numOfRepeats = minOf(first.count { it == el }, second.count { it == el } )
            repeat(numOfRepeats) { ans.add(el) }
        }
    }

    return ans
    
}


fun main() {
    println(*intersection([1, 2, 3, 2, 0], [1, 2, 2, 3]))
}