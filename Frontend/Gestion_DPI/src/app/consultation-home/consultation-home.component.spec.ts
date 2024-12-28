import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConsultationHomeComponent } from './consultation-home.component';

describe('ConsultationHomeComponent', () => {
  let component: ConsultationHomeComponent;
  let fixture: ComponentFixture<ConsultationHomeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ConsultationHomeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ConsultationHomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
