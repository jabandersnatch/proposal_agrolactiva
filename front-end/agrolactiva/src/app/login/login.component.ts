import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms'
import { first } from 'rxjs/operators';
import { PersonService } from '../services/person.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  myform: FormGroup;

  constructor(private personService: PersonService) { }

  ngOnInit() {
    this.myform = new FormGroup({
      username: new FormControl(''),
      password: new FormControl('')
    })
  }

  get f() {
    return this.myform.controls;
  }

  onSubmit() {
    this.personService.login(this.f['username'].value, this.f['password'].value).pipe(first()).subscribe(
      data => {
        console.log(data)
      }
    )
  }

}
