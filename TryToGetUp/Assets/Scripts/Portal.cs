using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Portal : MonoBehaviour
{
    void OnTriggerEnter2D(Collider2D other) {
        Debug.Log("Idziesz na kolejne piętro!");
    }
}
