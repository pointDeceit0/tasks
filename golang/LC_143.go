package main

import (
	//"fmt"
)

type ListNode struct {
    Val int
    Next *ListNode
}


func reorderList(head *ListNode) {
    // take reverse ll and iterate with two pointers for both of the lists, O(n) + O(2n) ~ O(n)
	middle := getMiddleElement(head) 
	tale := reverseList(middle)
	
	middle.Next = nil
	cur := head

	for tale != nil && cur != nil {
		temp1 := cur.Next
		temp2 := tale.Next
		cur.Next = tale
		tale.Next = temp1
		cur = temp1
		tale = temp2
	}
}

func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil { return nil }

	var tale *ListNode

	for head != nil {
		temp := head.Next
		head.Next = tale
		tale = head
		head = temp
	}
	return tale
}

func getMiddleElement(head *ListNode) *ListNode {

	if head == nil || head.Next == nil { return nil }
	slow, fast := head, head.Next

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	return slow
}


func test() {
	//n5 := &ListNode{Val: 5,}
	n4 := &ListNode{Val: 4}
	n3 := &ListNode{3, n4,}
	n2 := &ListNode{2, n3,}
	n1 := &ListNode{1, n2,}

	reorderList(n1)
}


func main() {
	test()
}
