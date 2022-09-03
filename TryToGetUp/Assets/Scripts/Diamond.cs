using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Diamond : MonoBehaviour
{
    [SerializeField] Color32 hasDiamondColor = new Color32(1, 1, 1, 1);
    
    bool hasDiamond = false;

    SpriteRenderer spriteRenderer;

    private void Start() {
        spriteRenderer = GetComponent<SpriteRenderer>();
    }

    void OnTriggerEnter2D(Collider2D other) {

            Debug.Log("Zebrałeś Diament!");    
            hasDiamond = true;
            spriteRenderer.color = hasDiamondColor;
    }
}
