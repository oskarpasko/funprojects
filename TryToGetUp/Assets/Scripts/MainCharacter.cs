using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MainCharacter : MonoBehaviour
{
 
    [SerializeField] float moveSpeed = 10f;
    [SerializeField] float jumpHeight = 4f;

    // Update is called once per frame
    void Update()
    {
        float moveAmount = Input.GetAxis("Horizontal") * moveSpeed * Time.deltaTime;
        transform.Translate(moveAmount, 0, 0);

        if(Input.GetKeyDown(KeyCode.W))  //makes player jump
        {
            GetComponent<Rigidbody2D>().AddForce(new Vector2(0, jumpHeight), ForceMode2D.Impulse);
        }
    }
}
