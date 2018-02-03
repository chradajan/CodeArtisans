using System.Collections;
using System.Collections.Generic;
using UnityEngine.SceneManagement;
using UnityEngine;

public class join_button : MonoBehaviour {

	public void joinGameScreen(){
		SceneManager.LoadScene("JoinGame");
		Debug.Log("hello");
	}
}
