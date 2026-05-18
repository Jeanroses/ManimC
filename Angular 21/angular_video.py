from manim import *
import numpy as np

BACKGROUND_COLOR = "#000000"
PRIMARY_COLOR = "#89b4fa"
SECONDARY_COLOR = "#f5c2e7"
ACCENT_COLOR = "#a6e3a1"
HIGHLIGHT_COLOR = "#f9e2af"
CURVE_COLOR = "#f38ba8"
TEXT_COLOR = "#cdd6f4"
WARNING_COLOR = "#fab387"
SUCCESS_COLOR = "#a6e3a1"
ITER_COLOR = "#cba6f7"
ANGULAR_COLOR = "#DD0031"
TYPESCRIPT_COLOR = "#3178C6"

config.background_color = BACKGROUND_COLOR


class IntroScene(Scene):
    def construct(self):
        title = Text(
            "Angular 21",
            font_size=58,
            color=ANGULAR_COLOR,
            line_spacing=1.2,
        ).set_color_by_gradient(ANGULAR_COLOR, PRIMARY_COLOR)

        subtitle = Text(
            "Framework enterprise para aplicaciones web modernas",
            font_size=26,
            color=TEXT_COLOR,
        ).next_to(title, DOWN, buff=0.7)

        dots = VGroup(*[
            Dot(radius=0.07, color=c)
            for c in [ANGULAR_COLOR, PRIMARY_COLOR, ACCENT_COLOR, HIGHLIGHT_COLOR]
        ])
        dots.arrange(RIGHT, buff=0.4).next_to(subtitle, DOWN, buff=0.6)

        self.play(Write(title, run_time=2.2))
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.2),
            run_time=1.2,
        )
        self.wait(0.8)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(dots),
            run_time=1.0,
        )


class AngularHistoryScene(Scene):
    def construct(self):
        title = Text("Historia de Angular", font_size=44, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        timeline = VGroup(
            Text("2010: AngularJS 1.0 - Framework JavaScript original", font_size=20, color=TEXT_COLOR),
            Text("2012: AngularJS 1.x series - Directives, services", font_size=20, color=TEXT_COLOR),
            Text("2016: Angular 2 - Complete rewrite, TypeScript", font_size:22, color=ANGULAR_COLOR),
            Text("2017: Angular 4, 5 - Performance improvements", font_size=20, color=TEXT_COLOR),
            Text("2019: Angular 8 - Ivy renderer preview, lazy loading", font_size:20, color=TEXT_COLOR),
            Text("2020: Angular 9 - Ivy by default, strict typing", font_size:20, color=TEXT_COLOR),
            Text("2022: Angular 14-16 - Standalone components, signals", font_size:20, color=HIGHLIGHT_COLOR),
            Text("2024: Angular 17-18 - Hydration, SSR improvements", font_size:20, color=SUCCESS_COLOR),
            Text("2025: Angular 21 - Latest with zoneless, deferrable views", font_size:20, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        timeline.next_to(title, DOWN, buff=0.7)

        self.play(Write(title), run_time=1)
        for t in timeline:
            self.play(FadeIn(t, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class AngularArchitectureScene(Scene):
    def construct(self):
        title = Text("Arquitectura de Angular", font_size=44, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        modules = '''// Module-based architecture (legacy)
@NgModule({
  declarations: [AppComponent, ChildComponent],
  imports: [BrowserModule, FormsModule, HttpClientModule],
  providers: [UserService],
  bootstrap: [AppComponent]
})
export class AppModule {}'''

        standalone = '''// Standalone components (modern)
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Mi Aplicacion';
}

// No more AppModule needed
bootstrapApplication(AppComponent, appConfig).catch(err => console.error(err));'''

        module_code = Code(
            code_string=modules,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        module_code.scale(0.75).to_edge(LEFT, buff=0.4).shift(UP * 0.5)

        standalone_code = Code(
            code_string=standalone,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        standalone_code.scale(0.75).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(module_code), run_time=1)
        self.play(Create(standalone_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class TypeScriptBasicsScene(Scene):
    def construct(self):
        title = Text("TypeScript Fundamentals", font_size=44, color=TYPESCRIPT_COLOR)
        title.to_edge(UP, buff=0.5)

        basics = '''// Primitive types
let nombre: string = 'Juan';
let edad: number = 25;
let activo: boolean = true;
let anything: any = 'puede ser cualquier cosa';

// Arrays
let numeros: number[] = [1, 2, 3, 4, 5];
let nombres: Array<string> = ['Juan', 'Maria'];
let mixto: (string | number)[] = [1, 'dos', 3];

// Objects
interface Usuario {
  id: number;
  nombre: string;
  email?: string;  // optional
  rol: 'admin' | 'user' | 'guest';
}

const usuario: Usuario = {
  id: 1,
  nombre: 'Juan',
  rol: 'admin'
};'''

        ts_code = Code(
            code_string=basics,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        ts_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class TypeScriptAdvancedScene(Scene):
    def construct(self):
        title = Text("TypeScript Avanzado", font_size=44, color=TYPESCRIPT_COLOR)
        title.to_edge(UP, buff=0.5)

        advanced = '''// Generics
function identidad<T>(valor: T): T {
  return valor;
}
const resultado = identidad<string>('hola');

// Classes
class Persona {
  constructor(
    public nombre: string,
    private edad: number
  ) {}

  getEdad(): number { return this.edad; }
}

// Enums
enum DiaSemana {
  Lunes = 'LUN',
  Martes = 'MAR',
  Miercoles = 'MIER'
}

// Union Types
type StringOrNumber = string | number;
type Result<T> = { success: true; data: T } | { success: false; error: string };

// Type Guards
function isString(val: unknown): val is string {
  return typeof val === 'string';
}

// Utility Types
type PartialUsuario = Partial<Usuario>;
type ReadonlyUsuario = Readonly<Usuario>;
type PickName = Pick<Usuario, 'nombre' | 'email'>;'''

        ts_code = Code(
            code_string=advanced,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        ts_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ComponentsScene(Scene):
    def construct(self):
        title = Text("Components", font_size=48, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        component = '''@Component({
  selector: 'app-user-card',
  standalone: true,
  imports: [CommonModule, DatePipe],
  template: `
    <div class="card" [class.active]="user.active">
      <h2>{{ user.name }}</h2>
      <p>Email: {{ user.email }}</p>
      <span>{{ user.joinedDate | date:'medium' }}</span>
    </div>
  `,
  styles: [`
    .card { padding: 16px; border: 1px solid #ccc; }
    .active { border-color: green; }
  `]
})
export class UserCardComponent {
  @Input() user!: User;
  @Input() showDetails = false;
  @Output() userSelected = new EventEmitter<User>();

  onSelect() {
    this.userSelected.emit(this.user);
  }
}'''

        ts_code = Code(
            code_string=component,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        ts_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ComponentLifecycleScene(Scene):
    def construct(self):
        title = Text("Ciclo de Vida de Componentes", font_size=40, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        lifecycle = '''export class MyComponent implements OnInit, OnChanges, OnDestroy {
  @Input() data: any;

  // Se ejecuta una vez al inicializar el componente
  ngOnInit() {
    console.log('Componente inicializado');
    this.loadData();
  }

  // Se ejecuta cuando cambia un input
  ngOnChanges(changes: SimpleChanges) {
    console.log('Cambios detectados:', changes);
    if (changes['data']) {
      this.processData(changes['data'].currentValue);
    }
  }

  // Se ejecuta antes de destruir el componente
  ngOnDestroy() {
    console.log('Limpiando recursos...');
    this.subscription?.unsubscribe();
  }

  loadData() { /* ... */ }
  processData(data: any) { /* ... */ }
}

// Other lifecycle hooks:
// ngAfterViewInit, ngAfterViewChecked
// ngAfterContentInit, ngAfterContentChecked'''

        ts_code = Code(
            code_string=lifecycle,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        ts_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DirectivesScene(Scene):
    def construct(self):
        title = Text("Directivas", font_size=48, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        attribute = '''// Attribute Directives
<div [ngClass]="{'active': isActive, 'disabled': isDisabled}">
<div [ngStyle]="{'color': textColor, 'font-size.px': fontSize}">

// Custom attribute directive
@Directive({ selector: '[appHighlight]' })
export class HighlightDirective {
  @Input('appHighlight') highlightColor = 'yellow';

  constructor(private el: ElementRef, private renderer: Renderer2) {}

  @HostListener('mouseenter') onMouseEnter() {
    this.renderer.setStyle(this.el.nativeElement, 'background-color', this.highlightColor);
  }

  @HostListener('mouseleave') onMouseLeave() {
    this.renderer.removeStyle(this.el.nativeElement, 'background-color');
  }
}'''

        structural = '''// Structural Directives
*ngIf
<div *ngIf="showContent">Contenido condicional</div>
<div *ngIf="show; else noContent">Contenido</div>
<ng-template #noContent>No hay contenido</ng-template>

*ngFor
<li *ngFor="let item of items; trackBy: trackById; let i = index">
  {{ i + 1 }}. {{ item.name }}
</li>

*ngSwitch
<div [ngSwitch]="user.role">
  <div *ngSwitchCase="'admin'">Admin panel</div>
  <div *ngSwitchCase="'user'">User panel</div>
  <div *ngSwitchDefault>Guest panel</div>
</div>

// @if and @for (Angular 17+)
@if (show) { <div>Contenido</div> }
@for (item of items; track item.id) { <li>{{ item.name }}</li> }'''

        attr_code = Code(
            code_string=attribute,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        attr_code.scale(0.75).to_edge(LEFT, buff=0.3).shift(UP * 0.3)

        struct_code = Code(
            code_string=structural,
            language="html",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        struct_code.scale(0.75).to_edge(RIGHT, buff=0.3).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(attr_code), run_time=1)
        self.play(Create(struct_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class PipesScene(Scene):
    def construct(self):
        title = Text("Pipes", font_size=48, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        built_in = '''// Built-in Pipes
{{ name | uppercase }}                      // JUAN
{{ name | lowercase }}                      // juan
{{ price | currency:'USD':'symbol':'1.2-2' }} // $1,234.57
{{ date | date:'mediumDate' }}               // Jan 15, 2024
{{ percentage | percent:'1.0-1' }}          // 12.3%
{{ jsonData | json }}                        // JSON formatted
{{ text | slice:0:10 }}                       // First 10 chars

// Chaining pipes
{{ user.createdAt | date:'short' | uppercase }}

<!-- Async pipe -->
<div>{{ observable$ | async }}</div>

<!-- Custom pipe -->
@Pipe({ name: 'appCapitalize' })
export class CapitalizePipe implements PipeTransform {
  transform(value: string): string {
    if (!value) return '';
    return value.charAt(0).toUpperCase() + value.slice(1);
  }
}

// Usage
{{ 'hola mundo' | appCapitalize }}  // Hola mundo'''

        ts_code = Code(
            code_string=built_in,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        ts_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DataBindingScene(Scene):
    def construct(self):
        title = Text("Data Binding", font_size=48, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        binding = '''// One-way binding
// From component to template
{{ title }}                                    // Interpolation
<img [src]="imageUrl">                        // Property binding
<button [disabled]="isDisabled">Click</button>

// From template to component
<input (input)="onInput($event)">             // Event binding
<input (click)="onClick()">

// Two-way binding (FormsModule)
<input [(ngModel)]="username">

// Two-way with binding
<input [ngModel]="name" (ngModelChange)="name = $event">

// Template reference
<input #searchInput placeholder="Search">
<button (click)="doSearch(searchInput.value)">Search</button>

// Binding to component
@Input() data: any;
@Output() action = new EventEmitter<void>();
@ViewChild('content') content!: ElementRef;
@ContentChild(CardComponent) card!: CardComponent;'''

        ts_code = Code(
            code_string=binding,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        ts_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class FormsScene(Scene):
    def construct(self):
        title = Text("Angular Forms", font_size=44, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        template_driven = '''// Template-driven Forms
import { FormsModule } from '@angular/forms';

<form #form="ngForm" (ngSubmit)="onSubmit(form)">
  <input
    type="text"
    name="username"
    [(ngModel)]="user.username"
    required
    minlength="3"
    #username="ngModel"
  >
  <div *ngIf="username.touched && username.errors">
    {{ username.errors | json }}
  </div>

  <input
    type="email"
    name="email"
    [(ngModel)]="user.email"
    email
    #email="ngModel"
  >

  <select name="country" [(ngModel)]="user.country">
    <option value="">Seleccionar</option>
    <option *ngFor="let c of countries" [value]="c.code">
      {{ c.name }}
    </option>
  </select>

  <button type="submit" [disabled]="form.invalid">Enviar</button>
</form>'''

        reactive = '''// Reactive Forms
import { ReactiveFormsModule } from '@angular/forms';
import { FormBuilder, Validators } in 'src/app/form.component.ts';

export class FormComponent implements OnInit {
  form!: FormGroup;

  constructor(private fb: FormBuilder) {}

  ngOnInit() {
    this.form = this.fb.group({
      username: ['', [Validators.required, Validators.minLength(3)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]],
      country: ['', Validators.required],
      terms: [false, Validators.requiredTrue]
    });
  }

  onSubmit() {
    if (this.form.valid) {
      const formData = this.form.value;
      // process form data
    }
  }

  get username() { return this.form.get('username'); }
}

// Template
<form [formGroup]="form" (ngSubmit)="onSubmit()">
  <input formControlName="username">
  <div *ngIf="username?.touched && username?.errors">
    {{ username?.errors | json }}
  </div>
</form>'''

        template_code = Code(
            code_string=template_driven,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        template_code.scale(0.75).to_edge(LEFT, buff=0.4).shift(UP * 0.3)

        reactive_code = Code(
            code_string=reactive,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        reactive_code.scale(0.75).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(template_code), run_time=1)
        self.play(Create(reactive_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ServicesScene(Scene):
    def construct(self):
        title = Text("Services e Inyeccion de Dependencias", font_size=38, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        service = '''@Injectable({ providedIn: 'root' })
export class UserService {
  private apiUrl = 'https://api.example.com/users';
  private http = inject(HttpClient);

  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(this.apiUrl);
  }

  getUserById(id: number): Observable<User> {
    return this.http.get<User>(`${this.apiUrl}/${id}`);
  }

  createUser(user: CreateUserDto): Observable<User> {
    return this.http.post<User>(this.apiUrl, user);
  }

  updateUser(id: number, user: UpdateUserDto): Observable<User> {
    return this.http.put<User>(`${this.apiUrl}/${id}`, user);
  }

  deleteUser(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}

// Injection en componente
@Component({...})
export class UserListComponent {
  private userService = inject(UserService);

  users$ = this.userService.getUsers();
}

// Injection por constructor (legacy)
constructor(private userService: UserService) {}'''

        ts_code = Code(
            code_string=service,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        ts_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class HttpClientScene(Scene):
    def construct(self):
        title = Text("HttpClient", font_size=48, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        http = '''// Configuracion global
export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(
      withFetch(),
      withInterceptors([authInterceptor, errorInterceptor])
    ),
    withRouter()
  ]
};

// Interceptors
@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const token = this.authService.getToken();
    if (token) {
      req = req.clone({
        setHeaders: { Authorization: `Bearer ${token}` }
      });
    }
    return next.handle(req);
  }
}

// Uso basico
@Injectable({ providedIn: 'root' })
export class ApiService {
  private http = inject(HttpClient);
  private baseUrl = 'https://api.example.com';

  get<T>(endpoint: string, options?: RequestOptions): Observable<T> {
    return this.http.get<T>(`${this.baseUrl}/${endpoint}`, options);
  }

  post<T>(endpoint: string, body: any, options?: RequestOptions): Observable<T> {
    return this.http.post<T>(`${this.baseUrl}/${endpoint}`, body, options);
  }

  put<T>(endpoint: string, body: any): Observable<T> {
    return this.http.put<T>(`${this.baseUrl}/${endpoint}`, body);
  }

  delete(endpoint: string): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/${endpoint}`);
  }

  // With headers
  getWithAuth<T>(endpoint: string): Observable<T> {
    return this.http.get<T>(endpoint, {
      headers: new HttpHeaders({
        'Authorization': 'Bearer token',
        'Custom-Header': 'value'
      })
    });
  }
}'''

        ts_code = Code(
            code_string=http,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        ts_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class RoutingScene(Scene):
    def construct(self):
        title = Text("Routing", font_size=48, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        routes = '''// app.routes.ts
export const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  {
    path: 'home',
    component: HomeComponent,
    title: 'Home - My App'
  },
  {
    path: 'users',
    loadComponent: () => import('./users/users.component').then(m => m.UsersComponent),
    canActivate: [AuthGuard],
    canActivateChild: [PermissionGuard],
    children: [
      { path: '', component: UserListComponent },
      { path: ':id', component: UserDetailComponent }
    ]
  },
  {
    path: 'admin',
    loadChildren: () => import('./admin/admin.routes').then(m => m.ADMIN_ROUTES),
    canActivate: [AdminGuard]
  },
  { path: '**', component: NotFoundComponent }
];

// Router Outlet
<router-outlet></router-outlet>

// Navigation
<a routerLink="/users" routerLinkActive="active">Users</a>
<a [routerLink]="['/users', user.id]" [queryParams]="{tab: 'details'}">User</a>

// Programmatic navigation
export class MyComponent {
  private router = inject(Router);

  navigate() {
    this.router.navigate(['/users', id], { queryParams: { tab: 'info' } });
  }

  navigateWithState() {
    this.router.navigate(['/details'], { state: { data: userData } });
  }

  getCurrentRoute() {
    const url = this.router.url;
    const params = this.router.snapshot.params;
    const queryParams = this.router.snapshot.queryParams;
  }
}'''

        ts_code = Code(
            code_string=routes,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        ts_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class RouteGuardsScene(Scene):
    def construct(self):
        title = Text("Route Guards", font_size=48, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        guards = '''// CanActivate - Protege ruta
@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {
  constructor(private router: Router, private authService: AuthService) {}

  canActivate(route: Route, segments: UrlSegment[]): boolean {
    if (this.authService.isAuthenticated()) {
      return true;
    }
    this.router.navigate(['/login']);
    return false;
  }
}

// CanActivateFn (functional)
export const authGuardFn: CanActivateFn = (route, segments) => {
  const authService = inject(AuthService);
  const router = inject(Router);

  if (authService.isAuthenticated()) {
    return true;
  }
  return router.createUrlTree(['/login']);
};

// CanDeactivate - Evita salida
export interface CanDeactivateComponent {
  canDeactivate(): Observable<boolean> | Promise<boolean> | boolean;
}

@Injectable({ providedIn: 'root' })
export class UnsavedChangesGuard implements CanDeactivate<CanDeactivateComponent> {
  canDeactivate(component: CanDeactivateComponent): boolean {
    return component.canDeactivate ? component.canDeactivate() : true;
  }
}

// Resolve - Pre-carga datos
@Injectable({ providedIn: 'root' })
export class UserResolver implements Resolve<User> {
  constructor(private userService: UserService, private router: Router) {}

  resolve(route: Route, state: RouterStateSnapshot): Observable<User> {
    const id = route.paramMap.get('id');
    if (!id) {
      this.router.navigate(['/users']);
      return EMPTY;
    }
    return this.userService.getUser(+id).pipe(
      catchError(() => {
        this.router.navigate(['/users']);
        return EMPTY;
      })
    );
  }
}

// Usage in routes
{ path: 'user/:id', component: UserDetailComponent, resolve: { user: UserResolver } }

// In component
export class UserDetailComponent implements OnInit {
  user = inject(ActivatedRoute).snapshot.data['user'];
  // or
  data$ = inject(ActivatedRoute).data;
}'''

        ts_code = Code(
            code_string=guards,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        ts_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class StateManagementScene(Scene):
    def construct(self):
        title = Text("State Management", font_size=48, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        signals = '''// Angular Signals (Angular 16+)
import { signal, computed, effect, WritableSignal } from '@angular/core';

// Signal basico
const count: WritableSignal<number> = signal(0);
const doubleCount = computed(() => count() * 2);

// Computed
const user = signal<User | null>(null);
const userName = computed(() => user()?.name ?? 'Guest');

// Efectos
effect(() => {
  console.log('Count changed:', count());
});

effect(() => {
  document.title = `Count: ${count()}`;
});

// Modificar signals
count.set(5);
count.update(c => c + 1);

// En componentes
@Component({...})
export class CounterComponent {
  count = signal(0);
  doubleCount = computed(() => this.count() * 2);

  increment() {
    this.count.update(c => c + 1);
  }
}

// Template
{{ count() }}
{{ doubleCount() }}'''

        ngrx = '''// NgRx Store
import { createAction, createReducer, on, props, createSelector } from '@ngrx/store';

// Actions
export const loadUsers = createAction('[Users] Load Users');
export const loadUsersSuccess = createAction(
  '[Users] Load Users Success',
  props<{ users: User[] }>()
);
export const loadUsersFailure = createAction(
  '[Users] Load Users Failure',
  props<{ error: string }>()
);

// State
export interface UsersState {
  users: User[];
  loading: boolean;
  error: string | null;
}

const initialState: UsersState = {
  users: [],
  loading: false,
  error: null
};

// Reducer
export const usersReducer = createReducer(
  initialState,
  on(loadUsers, state => ({ ...state, loading: true })),
  on(loadUsersSuccess, (state, { users }) => ({
    ...state,
    users,
    loading: false
  })),
  on(loadUsersFailure, (state, { error }) => ({
    ...state,
    error,
    loading: false
  }))
);

// Selectors
export const selectUsers = (state: AppState) => state.users.users;
export const selectUsersLoading = (state: State) => state.users.loading;

// Usage in component
@Component({...})
export class UsersComponent {
  private store = inject(Store);
  users$ = this.store.select(selectUsers);
  loading$ = this.store.select(selectUsersLoading);

  loadUsers() {
    this.store.dispatch(loadUsers());
  }
}'''

        signals_code = Code(
            code_string=signals,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        signals_code.scale(0.75).to_edge(LEFT, buff=0.3).shift(UP * 0.3)

        ngrx_code = Code(
            code_string=ngrx,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        ngrx_code.scale(0.75).to_edge(RIGHT, buff=0.3).shift(DOWN * 0.5)

        self.play(Write(title), run_time=1)
        self.play(Create(signals_code), run_time=1)
        self.play(Create(ngrx_code), run_time=1)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class DI_Scene(Scene):
    def construct(self):
        title = Text("Dependency Injection", font_size=44, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        di = '''// ProvidedIn: root (singleton global)
@Injectable({ providedIn: 'root' })
export class GlobalService {}

// ProvidedIn: any (nueva instancia por modulo)
@Injectable({ providedIn: 'any' })
export class ModuleService {}

// Inject decorador
@Component({...})
export class MyComponent {
  private service = inject(MyService);  // Moderno
  private router = inject(Router);
}

// Constructor injection (legacy)
constructor(
  private myService: MyService,
  private router: Router
) {}

// UseClass - Reemplazar implementacion
providers: [
  { provide: UserService, useClass: MockUserService }
]

// UseExisting - Alias
providers: [
  { provide: LoggerService, useExisting: ConsoleLogger }
]

// UseFactory - Factory function
providers: [
  {
    provide: AuthService,
    useFactory: (http: HttpClient, config: Config) =>
      new AuthService(http, config.apiUrl),
    deps: [HttpClient, ConfigService]
  }
]

// UseValue - Valores constante
providers: [
  { provide: APP_CONFIG, useValue: { apiUrl: 'https://api.com' } }
]'''

        ts_code = Code(
            code_string=di,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        ts_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SignalsScene(Scene):
    def construct(self):
        title = Text("Angular Signals - Reactive Primitive", font_size=38, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        advanced_signals = '''// Signal effects cleanup
effect(() => {
  console.log('Value:', this.signal());

  return () => {
    console.log('Cleanup for signal');
  };
});

// toSignal - Convert Observable a Signal
import { toSignal } from '@angular/core/rxjs-interop';

@Component({...})
export class UsersComponent {
  private userService = inject(UserService);

  // From Observable
  users = toSignal(this.userService.getUsers(), { initialValue: [] });

  // From Promise
  data = toSignal(this.fetchData(), { initialValue: null });

  // toObservable - Signal to Observable
  private counter = signal(0);
  counter$ = toObservable(this.counter);
}

// RxJS interop
import { toObservable, toStream } from '@angular/core/rxjs-interop';

@Component({...})
export class App {
  // Signal to Observable
  count = signal(0);
  count$ = toObservable(this.count);

  // combineLatest with signals
  a = signal(1);
  b = signal(2);
  combined = combineLatest([this.a, this.b]);

  // switchMap with signals
  userId = signal<string | null>(null);
  user$ = toObservable(this.userId).pipe(
    switchMap(id => id ? this.userService.getUser(id) : of(null))
  );
  user = toSignal(this.user$);
}

// Signal-based resources (@defer)
@defer (on viewport) {
  <heavy-component />
} @loading {
  Loading...
} @placeholder {
  Placeholder
} @error {
  Error loading
}'''

        ts_code = Code(
            code_string=advanced_signals,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        ts_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SSR_Scene(Scene):
    def construct(self):
        title = Text("Server-Side Rendering (SSR)", font_size=42, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        hydration = '''// Angular Universal / SSR
// ng add @angular/ssr

// Server-only code
import { isPlatformServer } from '@angular/common';

@Component({...})
export class MyComponent {
  constructor(@Inject(PLATFORM_ID) private platformId: Object) {
    if (isPlatformServer(this.platformId)) {
      // Solo en servidor
      console.log('Running on server');
    }
  }
}

// TransferState - Share data between server and client
import { TransferState, makeStateKey };

const USER_KEY = makeStateKey<User>('USER_DATA');

@Component({...})
export class UserComponent implements OnInit {
  private transferState = inject(TransferState);

  ngOnInit() {
    // Check if data already exists (transferred from server)
    if (this.transferState.hasKey(USER_KEY)) {
      this.user = this.transferState.get(USER_KEY, null as any);
    } else {
      this.userService.getUser().subscribe(user => {
        this.user = user;
        this.transferState.set(USER_KEY, user);
      });
    }
  }
}

// Hydration
// app.config.ts
export const appConfig: ApplicationConfig = {
  providers: [
    provideClientHydration()
  ]
};

// Non-destructive hydration
// Angular 17+ enables this by default

// TransferHttpCache - Cache HTTP responses
import { TransferHttpCacheModule } from '@angular/common/platform-server';

// app.server.module.ts
@NgModule({
  imports: [AppModule, TransferHttpCacheModule],
  bootstrap: [AppComponent]
})
export class AppServerModule {}'''

        ts_code = Code(
            code_string=hydration,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        ts_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class TestingScene(Scene):
    def construct(self):
        title = Text("Testing en Angular", font_size=44, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        unit_test = '''// Unit Test with Jest
describe('UserService', () => {
  let service: UserService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [UserService]
    });
    service = TestBed.inject(UserService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should get users', () => {
    const mockUsers: User[] = [{ id: 1, name: 'Test' }];

    service.getUsers().subscribe(users => {
      expect(users).toEqual(mockUsers);
    });

    const req = httpMock.expectOne('/api/users');
    expect(req.request.method).toBe('GET');
    req.flush(mockUsers);
  });
});

// Component Test
describe('UserCardComponent', () => {
  let component: UserCardComponent;
  let fixture: ComponentFixture<UserCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UserCardComponent, NoopAnimationsModule]
    }).compileComponents();

    fixture = TestBed.createComponent(UserCardComponent);
    component = fixture.componentInstance;
    component.user = { id: 1, name: 'Test User', email: 'test@test.com' };
    fixture.detectChanges();
  });

  it('should display user name', () => {
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('.name')?.textContent).toContain('Test User');
  });

  it('should emit userSelected on click', () => {
    jest.spyOn(component.userSelected, 'emit');
    fixture.debugElement.query(By.css('button')).triggerEventHandler('click', null);
    expect(component.userSelected.emit).toHaveBeenCalledWith(component.user);
  });
});'''

        ts_code = Code(
            code_string=unit_test,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        ts_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class PerformanceScene(Scene):
    def construct(self):
        title = Text("Optimizacion de Rendimiento", font_size=40, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        optimization = '''// OnPush Change Detection
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class PureComponent {
  // Solo se re-renderiza cuando:
  // - Input reference changes
  // - Event handler triggered
  // - Async pipe emits
  // - Manual change detection triggered
}

// Manual change detection
constructor(private cdr: ChangeDetectorRef) {}

updateData() {
  this.data = this.calculateData();
  this.cdr.markForCheck();
}

// trackBy function
@Component({...})
export class ItemListComponent {
  trackById(index: number, item: any): number {
    return item.id;
  }
}

<li *ngFor="let item of items; trackBy: trackById">{{ item.name }}</li>

// Lazy loading
// Routes
{ path: 'admin', loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule) }

// Components
@Component({
  imports: [CommonModule, RouterModule],
  standalone: true
})
@Loadable(() => import('./heavy/heavy.component').then(m => m.HeavyComponent))
export class LightComponent {}

// Preloading strategies
export const routes: Routes = [{
  path: 'admin',
  loadChildren: () => import('./admin/admin.routes').then(m => m.ADMIN_ROUTES),
  data: { preload: true }
}];

providers: [
  provideRouter(routes, withPreloading(PreloadAllModules))
]

// Bundle analysis
ng build --stats-json
npx webpack-bundle-analyzer dist/app/stats.json'''}}

        ts_code = Code(
            code_string=optimization,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        ts_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class InterceptorsScene(Scene):
    def construct(self):
        title = Text("HTTP Interceptors", font_size=48, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        interceptors = '''// Functional interceptor
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const token = inject(AuthService).getToken();

  if (token) {
    const authReq = req.clone({
      headers: req.headers.set('Authorization', `Bearer ${token}`)
    });
    return next(authReq);
  }

  return next(req);
};

// Error handling interceptor
export const errorInterceptor: HttpInterceptorFn = (req, next) => {
  return next(req).pipe(
    catchError((error: HttpErrorResponse) => {
      if (error.status === 401) {
        inject(Router).navigate(['/login']);
      } else if (error.status === 403) {
        inject(ToastService).show('Access denied');
      }
      return throwError(() => error);
    })
  );
};

// Register interceptors
export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(
      withInterceptors([authInterceptor, errorInterceptor])
    )
  ]
};

// Class-based interceptor (legacy)
@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    // Logic
    return next.handle(req);
  }
}'''

        ts_code = Code(
            code_string=interceptors,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        ts_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class AnimationsScene(Scene):
    def construct(self):
        title = Text("Angular Animations", font_size=44, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        animations = '''// enableAnimations in app.config
export const appConfig: ApplicationConfig = {
  providers: [provideAnimations()]
};

// Component animations
@Component({
  selector: 'app-list',
  animations: [
    trigger('listAnimation', [
      transition(':enter', [
        style({ opacity: 0 }),
        animate('300ms', style({ opacity: 1 }))
      ]),
      transition(':leave', [
        animate('300ms', style({ opacity: 0 }))
      ]),
      transition('* => *', [
        style({ transform: 'translateX(-10px)', opacity: 0 }),
        animate('200ms')
      ])
    ]),
    trigger('expandCollapse', [
      transition(':enter', [
        style({ height: 0, opacity: 0 }),
        animate('300ms', style({ height: '*', opacity: 1 }))
      ]),
      transition(':leave', [
        animate('300ms', style({ height: 0, opacity: 0 }))
      ])
    ])
  ],
  template: `
    <ul>
      <li *ngFor="let item of items; @listAnimation">{{ item.name }}</li>
    </ul>
  `
})
export class ListComponent {}

// Router animations
export const routes: Routes = [{
  path: 'admin',
  component: AdminComponent,
  data: { animation: 'AdminPage' }
}];

// app.component.ts
@Component({
  selector: 'app-root',
  animations: [
    trigger('routeAnimations', [
      transition('* <=> *', [
        query(':enter, :leave', [
          style({
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%'
          })
        ], { optional: true }),
        query(':enter', [
          style({ opacity: 0 })
        ], { optional: true }),
        animate('300ms', style({ opacity: 1 }))
      ])
    ])
  ],
  template: `
    <div [@routeAnimations]="o.isActivated ? o.activatedRoute : ''">
      <router-outlet #o="outlet"></router-outlet>
    </div>
  `
})
export class AppComponent {}'''

        ts_code = Code(
            code_string=animations,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        ts_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class SignalsZonelessScene(Scene):
    def construct(self):
        title = Text("Zoneless Change Detection", font_size=42, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        zoneless = '''// Enable zoneless
export const appConfig: ApplicationConfig = {
  providers: [
    provideExperimentalZonelessChangeDetection()
  ]
};

// Works with Signals natively
@Component({
  selector: 'app-counter',
  standalone: true,
  template: `
    <button (click)="decrement()">-</button>
    <span>{{ count() }}</span>
    <button (click)="increment()">+</button>
  `
})
export class CounterComponent {
  count = signal(0);

  increment() {
    this.count.update(c => c + 1);
  }

  decrement() {
    this.count.update(c => c - 1);
  }
}

// Async pipe also works
@Component({
  selector: 'app-users',
  standalone: true,
  imports: [AsyncPipe, NgFor],
  template: `
    @for (user of users$ | async; track user.id) {
      <li>{{ user.name }}</li>
    }
  `
})
export class UsersComponent {
  private userService = inject(UserService);
  users$ = this.userService.getUsers();
}

// Auto-unsubscribe with takeUntilDestroyed
@Component({...})
export class MyComponent {
  private destroyRef = inject(DestroyRef);

  ngOnInit() {
    this.data$.pipe(
      takeUntilDestroyed(this.destroyRef)
    ).subscribe(data => this.processData(data));
  }
}

// Computed signals auto-unsubscribe
@Component({...})
export class DashboardComponent {
  private store = inject(Store);

  // Subscribes to userSignal and auto-unsubscribes on destroy
  user = toSignal(this.store.select(selectUser));

  // Auto-subscription with resource
  private data = resource({
    loader: () => this.fetchData()
  });
}'''

        ts_code = Code(
            code_string=zoneless,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        ts_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ControlFlowScene(Scene):
    def construct(self):
        title = Text("Control Flow Syntax (Angular 17+)", font_size=40, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        control_flow = '''// @if
@if (isLoggedIn) {
  <app-dashboard />
} @else {
  <app-login />
}

@if (user$ | async; as user) {
  <p>Bienvenido, {{ user.name }}</p>
} @else if (loading) {
  <app-spinner />
} @else {
  <app-error />
}

// @for
@for (item of items; track item.id; let i = $index) {
  <li>{{ i + 1 }}. {{ item.name }}</li>
} @empty {
  <p>No hay elementos</p>
}

// @switch
@switch (user.role) {
  @case ('admin') {
    <app-admin-panel />
  }
  @case ('editor') {
    <app-editor-panel />
  }
  @default {
    <app-viewer-panel />
  }
}

// @defer
@defer {
  <heavy-component [data]="data" />
} @loading {
  <app-spinner>Loading...</app-skeleton>
} @placeholder {
  <div>Componente pesado</div>
} @error {
  <p>Error al cargar</p>
}

// @defer on conditions
@defer (on viewport) {
  <chart-component />
} @placeholder {
  <div>Chart placeholder</div>
}

@defer (on hover) {
  <tooltip-component />
} @placeholder {
  Hover para ver
}

@defer (on timer(2000)) {
  <delayed-component />
} @placeholder {
  Loading in 2s...
}'''

        ts_code = Code(
            code_string=control_flow,
            language="html",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        ts_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class StandaloneScene(Scene):
    def construct(self):
        title = Text("Standalone Components Deep Dive", font_size=38, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        standalone_advanced = '''// Standalone component with providers
@Component({
  selector: 'app-scope',
  standalone: true,
  imports: [CommonModule],
  providers: [
    // Scoped service - singleton per component instance
    {
      provide: LocalService,
      useClass: LocalServiceImpl,
      deps: [SomeDep]
    },
    // Token
    {
      provide: 'API_URL',
      useValue: 'https://api.local.com'
    }
  ]
})
export class ScopeComponent {}

// Standalone with view providers
@Component({
  selector: 'app-isolate',
  standalone: true,
  viewProviders: [
    // For DOM interactions
    {
      provide: Renderer2,
      useFactory: () => inject(RendererFactory2).createRenderer(null, null)
    }
  ]
})
export class IsolateComponent {}

// Lazy loaded standalone component
// main.ts
bootstrapApplication(AppComponent, appConfig).catch(err => console.error(err));

// routes.ts
{
  path: 'admin',
  loadComponent: () => import('./admin/admin.component').then(m => m.AdminComponent)
}

// Import and use standalone in routes
// Using Routes with loadComponent
const routes: Routes = [
  {
    path: 'lazy',
    loadComponent: () => import('./lazy/lazy.component').then(c => c.LazyComponent)
  }
];

// Direct import (no routing)
const lazyComponent = import('./heavy/heavy.component').then(m => m.HeavyComponent);'''

        ts_code = Code(
            code_string=standalone_advanced,
            language="typescript",
            formatter_style="monokai",
            background="rectangle",
            font_size=16,
        )
        ts_code.scale(0.85).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class BuildDeployScene(Scene):
    def construct(self):
        title = Text("Build y Deployment", font_size=44, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        build = '''// Build commands
ng build                                    # Development build
ng build --configuration=production        # Production build
ng build --configuration=staging            # Staging build
ng build --optimization=true --source-map=false
ng build --named-chunks=false              # Disable named chunks

// Differential loading (Angular 12+)
# Disabled by default in v17+ (ESBuild)

// SSR Build
ng build && ng run app:server              # Universal
npm run build:ssr                           # With custom script

// Analysis
ng build --stats-json
npx webpack-bundle-analyzer dist/app/stats.json

// Environment-specific builds
# environment.ts (default)
# environment.prod.ts
# environment.staging.ts

# Build with environment
ng build --configuration=production

// Build as library
ng build my-lib
ng build my-lib --configuration=production

// Deploy
# Static hosting (Firebase, Vercel, Netlify)
ng deploy

# Docker
# Dockerfile
FROM node:20-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist/app /usr/share/nginx/html
EXPOSE 80'''

        ts_code = Code(
            code_string=build,
            language="bash",
            formatter_style="monokai",
            background="rectangle",
            font_size=18,
        )
        ts_code.scale(0.9).next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        self.play(Create(ts_code), run_time=1.5)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class NewFeaturesScene(Scene):
    def construct(self):
        title = Text("Angular 21+ Nuevas Caracteristicas", font_size=40, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.5)

        features = VGroup(
            Text("Zoneless Change Detection - Experimental", font_size=22, color=HIGHLIGHT_COLOR),
            Text("Deferrable Views (@defer) - Carga deferida de componentes", font_size=22, color=TEXT_COLOR),
            Text("Signal-based Resources - Recursos reactivos", font_size:22, color=TEXT_COLOR),
            Text("Control Flow (@if, @for, @switch) - Nueva sintaxis", font_size:22, color=TEXT_COLOR),
            Text("Standalone by Default - Todo es standalone", font_size:22, color=TEXT_COLOR),
            Text("ESBuild + Vite - Build mas rapido", font_size:22, color=TEXT_COLOR),
            Text("Hydration no destructiva - SSR mejorado", font_size22, color=TEXT_COLOR),
            Text("Angular Signals - Reactive primitive nativa", font_size22, color=TEXT_COLOR),
            Text("Functional Guards/Interceptors - Alternativa a clases", font_size22, color=TEXT_COLOR),
            Text("DestroyRef + takeUntilDestroyed - Auto-unsubscribe", font_size22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        features.next_to(title, DOWN, buff=0.6)

        self.play(Write(title), run_time=1)
        for f in features:
            self.play(FadeIn(f, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class ConclusionScene(Scene):
    def construct(self):
        title = Text("Resumen: Angular 21", font_size=42, color=ANGULAR_COLOR)
        title.to_edge(UP, buff=0.6)

        items = VGroup(
            Text("Angular: Framework enterprise de Google para SPAs", font_size=22, color=TEXT_COLOR),
            Text("TypeScript: Tipado estatico con caracteristicas modernas", font_size=22, color=TEXT_COLOR),
            Text("Components: Bloques fundamentales con lifecycle", font_size:22, color=TEXT_COLOR),
            Text("Directives: Estructurales y de atributo", font_size22, color=TEXT_COLOR),
            Text("Services & DI: Inyeccion de dependencias robusto", font_size22, color=TEXT_COLOR),
            Text("Forms: Template-driven y Reactive Forms", font_size22, color=TEXT_COLOR),
            Text("Routing: Navegacion con guards y resolvers", font_size22, color=TEXT_COLOR),
            Text("Signals: Nueva primitiva reactiva (Angular 16+)", font_size22, color=TEXT_COLOR),
            Text("SSR/Hydration: Server-side rendering con hydration", font_size22, color=TEXT_COLOR),
            Text("Testing: Jasmine/Jest para unit y e2e", font_size22, color=TEXT_COLOR),
            Text("Standalone: Componentes independientes sin NgModule", font_size22, color=TEXT_COLOR),
            Text("Zoneless: Cambio de deteccion experimental sin Zone.js", font_size22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        items.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)
        self.wait(1)

        final_msg = Text(
            "Framework dominante para aplicaciones enterprise complejas",
            font_size=26,
            color=ACCENT_COLOR,
        ).next_to(items, DOWN, buff=0.5)

        self.play(FadeIn(final_msg, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.9)


class AngularFullVideo(Scene):
    def construct(self):
        IntroScene.construct(self)
        AngularHistoryScene.construct(self)
        AngularArchitectureScene.construct(self)
        TypeScriptBasicsScene.construct(self)
        TypeScriptAdvancedScene.construct(self)
        ComponentsScene.construct(self)
        ComponentLifecycleScene.construct(self)
        DirectivesScene.construct(self)
        PipesScene.construct(self)
        DataBindingScene.construct(self)
        FormsScene.construct(self)
        ServicesScene.construct(self)
        HttpClientScene.construct(self)
        RoutingScene.construct(self)
        RouteGuardsScene.construct(self)
        StateManagementScene.construct(self)
        DI_Scene.construct(self)
        SignalsScene.construct(self)
        SSR_Scene.construct(self)
        TestingScene.construct(self)
        PerformanceScene.construct(self)
        InterceptorsScene.construct(self)
        AnimationsScene.construct(self)
        SignalsZonelessScene.construct(self)
        ControlFlowScene.construct(self)
        StandaloneScene.construct(self)
        BuildDeployScene.construct(self)
        NewFeaturesScene.construct(self)
        ConclusionScene.construct(self)