import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PageLaborantinComponent } from './page-laborantin.component';

describe('PageLaborantinComponent', () => {
  let component: PageLaborantinComponent;
  let fixture: ComponentFixture<PageLaborantinComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PageLaborantinComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PageLaborantinComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
